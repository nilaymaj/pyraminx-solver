import cli

def main():
  print("Welcome to the PyraminxSolver Testing Ground\n")
  pyraminx = cli.inputState()
  step = input("What is the rotation you want to make: ")
  pyraminx.move(step)
  cli.printState(pyraminx)
  pass

if __name__ == "__main__":
  main()