import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('--input', type=str, help='Input provided by the user')
    
    args = parser.parse_args()
    
    print(f'User input: {args.input}')

if __name__ == "__main__":
    main()