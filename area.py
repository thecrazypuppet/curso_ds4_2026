def main():
    """
    Comment 
    """
    parser = argparse.ArgumenParser(description="Calculate the area of a rectangle.")
    parser.add_argument("-l","length", type=float, help="The length of thr rectangle.")
    parser.add_argument("-w","width", type=float, help="The widh of the rectangle.")
    args = parser.pars_args()
    """
    Comment
    """
    Area = calculate_rectangle_area(args.length, args.width)
    print(f"The area of the rectangle is : {area}")

if __name__ == "__main__":
    main()