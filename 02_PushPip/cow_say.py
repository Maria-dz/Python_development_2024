import cowsay 
import argparse


if __name__ == "__main__":

    cow_parser = argparse.ArgumentParser()

    
    #eyes=Option.eyes – A custom eye string
    cow_parser.add_argument('-e', '--eyes', default=cowsay.Option.eyes)

    #tongue=Option.tongue – A custom tongue string
    cow_parser.add_argument('-T', '--tongue', default=cowsay.Option.tongue)

    #width=40 – The width of the text bubble
    cow_parser.add_argument('-W', '--width', default=40, type=int)

    #wrap_text=True – Whether text should be wrapped in the bubble
    cow_parser.add_argument('-n', '--wrap_text', action = 'store_true')

    #cowfile=None – A custom string representing a cow
    cow_parser.add_argument('-f', '--cowfile', default=None)

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
   
    #message – a string to wrap in the text bubble
    cow_parser.add_argument("custom_message", nargs='*', default=[' '])

    #parsing all income arguments
    args = cow_parser.parse_args()

    #default params
    cow = "default"
    cowfile = None
    wrap_text = True
    preset = None
    custom_message = ' '.join(args.custom_message)

    if args.cowfile:
        if  "/" in args.cowfile:
            cowfile = args.cowfile
        else:
            cow = args.cowfile
    
    if args.list:
        print(cowsay.list_cows())
    else:
        if args.wrap_text:
            wrap_text = False
        
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
    
        print(cowsay.cowsay(message=custom_message, cow=cow, preset=preset, eyes=args.eyes, tongue=args.tongue, width=args.width,
                  wrap_text=wrap_text, cowfile=cowfile))
