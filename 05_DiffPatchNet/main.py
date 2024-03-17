#!/usr/bin/env python3

import asyncio
import cowsay

clients = {}
all_available_cows = list(cowsay.list_cows())

async def chat(reader, writer):
    me = None # пока не зарегистрировался
    allowed = False # не доступна связь без регистрации

    cur_queue = asyncio.Queue()
    sended = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(cur_queue.get())

    while not reader.at_eof():
        done, _ = await asyncio.wait([sended, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is sended:
                # обработка команд
                all_args = q.result().decode().strip().split()
                sended = asyncio.create_task(reader.readline())

                # получаем команды и аргументы
                if len(all_args) > 1:
                    comand_name = all_args[0]
                    other_params = all_args[1:]

                    if comand_name == "login":
                        me = other_params[0]
                        if me not in all_available_cows:
                            writer.write("This login is unavailable, chose another one and try again\n".encode())
                            continue
                        if me in clients.keys():
                            writer.write("This login is already used, chose another one and try again\n".encode())
                            continue
                        clients[me] = cur_queue
                        writer.write("Now you can use cow-chat!\n".encode())
                        allowed = True

                    elif comand_name == "say":
                        if not allowed:
                            writer.write("Use <login [cowname]> command to register and be allowed to send messages in cow-chat\n".encode())
                        else:
                            receiver = other_params[0]
                            message = ' '.join(other_params[1:])
                            out = clients[receiver]
                            await out.put(f'{cowsay.cowsay(cow=me, message=message)}')

                    elif comand_name == "yield":
                        if not allowed:
                            writer.write("Use <login [cowname]> command to register and be allowed to send messages\n".encode())
                        else:
                            for out in clients.values():
                                if out is not cur_queue:
                                    message = ' '.join(other_params)
                                    await out.put(f'{cowsay.cowsay(cow=me, message=message)}')
                    else:
                        writer.write(f"Unknown command\n".encode())


                else:
                    comand_name = all_args[0]
                    if comand_name == "who":
                        if not allowed:
                            writer.write("Use <login [cowname]> command to register and be allowed to send messages in cow-chat\n".encode())
                        else:
                            writer.write(f"{' '.join(clients.keys())}\n".encode())

                    elif comand_name == "cows":
                        writer.write(f"{' '.join(set(all_available_cows) - set(clients.keys()))}\n".encode())

                    elif comand_name == "quit":
                        sended.cancel()
                        receive.cancel()
                        del clients[me]
                        writer.close()
                        await writer.wait_closed()

                    else:
                        writer.write(f"Unknown command\n".encode())
               
            elif q is receive:
                receive = asyncio.create_task(cur_queue.get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())