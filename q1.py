#q1
if _name_ == "_main_":

    # Get the number of available T-shirts and the list of available T-shirt sizes
  
    available_tshirts = input("")
    available_list = input("")

  # Get the number of requested T-shirts and the list of requested T-shirt sizes
  
    requested_tshirts = input("")
    requested_list = input("")

  # Split the input strings into lists of individual sizes
  
    final_list =     available_list.split(" ")
    final_requested_list = requested_list.split(" ")

  # Initialize a variable to keep track of whether all requests can be fulfilled

    can_provide = True

  # Iterate over each requested size and check if it can be fulfilled with an available size
    for i in final_requested_list:

      # Iterate over each available size and check if it matches the requested size
        for j in final_list:
          
            if ("S" in i and "S" in j) and i.count("X") >= j.count("X"):
                    break
            if ("S" in i and "M" in j):
                break
              
            elif ("S" in i and "L" in j):
                break
              
            elif ("M" in i and "M" in j):
                break
              
            elif ("M" in i and "L" in j):
                break
              
            elif ("L" in i and "L" in j) and i.count("X") <= j.count("X"):
                break
              # If a matching T-shirt was not found, set the flag to indicate that all requests cannot be fulfilled
            else:
                can_provide = False

              
    # Print the result based on whether all requests can be fulfilled or not            
    if can_provide == True:
      
        print("Yes")
      
    else:
        print("No")