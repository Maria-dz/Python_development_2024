import cowsay 
import argparse


if __name__ == "__main__":

    cow_parser = argparse.ArgumentParser()

    #message – a string to wrap in the text bubble
    cow_parser.add_argument('--message', default="", type=str)

    #cow='default' – the name of the cow (valid names from list_cows)
    cow_parser.add_argument('--cow', default="default", type=str)

    #eyes=Option.eyes – A custom eye string
    cow_parser.add_argument('--eyes', default=cowsay.Option.eyes)

    #tongue=Option.tongue – A custom tongue string
    cow_parser.add_argument('--tongue', default=cowsay.Option.tongue)

    #width=40 – The width of the text bubble
    cow_parser.add_argument('--width', default=40, type=int)

    #wrap_text=True – Whether text should be wrapped in the bubble
    cow_parser.add_argument('--wrap_text', default=True, type=bool)

    #cowfile=None – A custom string representing a cow
    cow_parser.add_argument('--cowfile', default=None)

    #adding -l argument 
    cow_parser.add_argument('-l', '--list', action='store_true')

    #parsing preset arguments
    cow_parser.add_argument('-b', action='store_true')
    cow_parser.add_argument('-d', action='store_true')
    cow_parser.add_argument('-g', action='store_true')
    cow_parser.add_argument('-p', action='store_true')
    cow_parser.add_argument('-s', action='store_true')
    cow_parser.add_argument('-t', action='store_true')
    cow_parser.add_argument('-w', action='store_true')
    cow_parser.add_argument('-y', action='store_true')


    #parsing all income arguments
    args = cow_parser.parse_args()
    print(args)

    if args.list:
        print(cowsay.list_cows())
    else:
        preset = None
        if args.b:
            preset = "b"
        elif args.d:
            preset = "d"
        elif args.g:
            preset = "g"
        elif args.p:
            preset = "p"
        elif args.s:
            preset = "s"
        elif args.t:
            preset = "t"
        elif args.w:
            preset = "w"
        elif args.y:
            preset = "y"
    
        print(cowsay.cowsay(message=args.message, cow=args.cow, preset=preset, eyes=args.eyes, tongue=args.tongue, width=args.width,
                  wrap_text=args.wrap_text, cowfile=args.cowfile))
