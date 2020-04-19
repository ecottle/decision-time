def printMainTaskPrompt(mainTask):
  input("\nAwesome! Let's break down " + mainTask + " into 2 to 5 subtasks. Press Enter to continue.")

def getLowerSubTasksOf(task):
  print("\nList the subtasks to complete " + task + " below. Type 'DONE' if you have less than 5 subtasks.")
  subTasks = []
  for i in range(1, 6):
    subTask = input(str(i) + '. ')
    if subTask.lower() == 'done':
      break
    else :
      subTasks.append(subTask)
  return subTasks

def ask(question, time, multiplier):
  answer = input(question + '\n')
  if answer.lower() == 'yes':
    pass
  elif answer.lower() == 'no':
    time = multiplier*time
  else:
    print("Please type yes or no to answer the question./n")
    time = ask(question, time, multiplier)
  return time

def estimateTimeOf(task):
  timeUserEst = int(input('How many hours will ' + task + ' take?\n'))
  timeAdustedEst = ask("Have you ever completed a similar task to " + task + " before?", timeUserEst, 1.1)
  return timeUserEst, timeAdustedEst

def decisionTime():
  #Welcome back
  #How accurate was the last prediction?
  #Rate your experience out of 5 stars
  #create a multiplier based on this information
  mainTask = input('What is the task you need to do? Enter it below.\n')
  printMainTaskPrompt(mainTask)

  firstLayerTasks = getLowerSubTasksOf(mainTask)
  
  input("\nGreat! Let's look into each subtask now. Press Enter to continue.")

  lowestLevelTasks = []

  for task in firstLayerTasks:
    secondLayerTasks = getLowerSubTasksOf(task)
    if not secondLayerTasks: 
      secondLayerTasks = [task]
    lowestLevelTasks.append(secondLayerTasks)

  input("\nNow that you know exactly what needs to be done, let's estimate the time needed to do each task. Press Enter to continue.")

  index = 0
  totalEstimation = 0
  totalAdjustedEstimation = 0
  for taskList in lowestLevelTasks:
    print("\nLet's look at " + firstLayerTasks[index] + ".")
    for task in taskList:
      timeUserEst, timeAdjustedEst = estimateTimeOf(task)
      totalEstimation = totalEstimation + timeUserEst
      totalAdjustedEstimation = totalAdjustedEstimation + timeAdjustedEst
    index = index + 1
  
  print("Nice work unpacking and estimating time! By unpacking, you estimated " + mainTask + " to take a total of " + str(totalEstimation) + " hours. Based on memory recall, we estimate the total time to be " + str(totalAdjustedEstimation) + " hours.")
