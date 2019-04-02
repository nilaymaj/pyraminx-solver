def missingNum(array, totalSum = 10):
  for i in array:
    totalSum -= i
  return totalSum

def getSwitcher(pyraminx):
  yellow = missingNum((pyraminx.red_face[0][0], pyraminx.green_face[0][1], pyraminx.blue_face[0][2]))
  red = missingNum((pyraminx.yellow_face[0][0], pyraminx.blue_face[0][1], pyraminx.green_face[0][2]))
  green = missingNum((pyraminx.blue_face[0][0], pyraminx.yellow_face[0][1], pyraminx.red_face[0][2]))
  blue = missingNum((pyraminx.green_face[0][0], pyraminx.red_face[0][1], pyraminx.yellow_face[0][2]))
  switcher = {yellow: 4, red: 1, green: 2, blue: 3}
  return switcher

def fixColors(pyraminx):
  switcher = getSwitcher(pyraminx)
  for i in range(3):
    for j in range(3):
      pyraminx.red_face[i][j] = switcher[pyraminx.red_face[i][j]]
      pyraminx.green_face[i][j] = switcher[pyraminx.green_face[i][j]]
      pyraminx.yellow_face[i][j] = switcher[pyraminx.yellow_face[i][j]]
      pyraminx.blue_face[i][j] = switcher[pyraminx.blue_face[i][j]]
  return pyraminx

