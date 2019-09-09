# Inter-Domain Routing Simulator

# Libraries for the graph and tkinter for the GUI
import networkx as nx
import matplotlib.pyplot as plt
#import seaborn as sb
from tkinter import *
import random
import sys
import pyautogui  # this libr\ary is used to diplay dialog boxes such an alert and prompt to communicate with the user.
from mpl_toolkits.basemap import Basemap as Basemap
import matplotlib.animation as animation


# Longitute is horizontal going from -180 to 180
# Latitude is vertical going from -90 to 90

# I should plot like (latitude, longitute, latlon = True)

fig = plt.figure(figsize=(9, 9), edgecolor='r')
m = Basemap(projection='mill',llcrnrlat=-46 , urcrnrlat=65, llcrnrlon=-20 , urcrnrlon=72)

# Configuring the GUI
main = Tk()
main.title("IRDP")
main.geometry("365x440")
main.config(bg = 'black')


# Initialize my Graph variable
G = nx.Graph()

pos1 = 0
pos2 = -30
pos3 = 10


# (Start) Define my functions below ---------------------------------------------------------------------------------------

def deploy_nodes():
    #getting user input from the text boxes
    
    plt.clf()
    
    node1 = node1_input_box.get()
    node2 = node2_input_box.get()
    weight_user = weight_spinner.get()
    tierType1 = var3.get()
    tierType2 = var4.get()
    node1_country = var.get()
    node2_country = var2.get()
    
    # Writing to the nodes.txt file
    file = open("nodes.txt", "a")
    file.write(node1 + "," + node2 + "," + weight_user + "," + tierType1 + "," + tierType2 + "," + node1_country + "," + node2_country + "," + "\n")
    file.close()
    
    # provide use with feedback after successfully inserting a pair of nodes
    
    pyautogui.alert('Successfully diployed'+" "+'node'+" " +node1+ " "+'and'+" " + node2,"Confirmation")
    
    # clear the text fields so use can insert another pair of nodes
    node1_input_box.delete(0, END)
    node2_input_box.delete(0,END)
    weight_input_box.delete(0,END)
    output.delete(0,END)
    #var.set("South Africa")
    #var2.set("South Africa")
    
def draw_graph():
        
    # denoting that these are globally institiated
    global pos1
    global pos2
    global pos3
    
    global var
    global var2
        
    # color map to maap different color for each node in a particular tier
    color_map = []
    
    t_one = []
    t_two = []
    t_three = []
    
    
    # reading from the nodes.txt file
    file = open("nodes.txt", "r")
    for line in file:
        path = line.split(",")
        
        # Get Nodes and Weight
        node1 = int(path[0])
        node2 = int(path[1])
        weight_user = path[2]
        
        # Assign colors to nodes, nodes in T1 = Red, T2 = Green, T3 = blue
        col = ''
        col2 = ''
        
        # Note on the UI x ranges from 0.971534 to 1.01547 & y ranges from 1.85451 to 2.01905 - This was before the map so its void now.
        
        # Getting the tier so i can display node in a suitable position in Graph interface
        node1_tier = int(path[3])
        node2_tier = int(path[4])
        
        if node1_tier == 1:           
            col = 'red'
            if node1 not in t_one:
                t_one.append(node1)
            
        elif node1_tier == 2:            
            col = 'green'
            if node1 not in t_two:
                t_two.append(node1)            
                        
        else:  
            col = 'blue'
            if node1 not in t_three:
                t_three.append(node1)            
        
        if node2_tier == 1:            
            col2 = 'red'
            if node2 not in t_one:
                t_one.append(node2)            
                       
        elif node2_tier == 2:            
            col2 = 'green'
            if node2 not in t_two:
                t_two.append(node2)             
                       
        else:
            col2 = 'blue'
            if node2 not in t_three:
                t_three.append(node2)             

        if(path[5] == "South Africa"):
            node1_y = -29.16895
            node1_x = 26.568181
        elif(path[5] == "Zimbabwe"):
            node1_y = -19.329287
            node1_x = 30.170774
        elif(path[5]  == "Congo"):
            node1_y = -2.479389
            node1_x = 23.987360
        elif(path[5]  == "Mozambique"):
            node1_y = -18.164121
            node1_x = 35.673637
        elif(path[5]  == "Botswana"):
            node1_y = -22.773649
            node1_x = 24.075226
        elif(path[5]  == "Malawi"):
            node1_y = -13.856747
            node1_x = 34.092036  
        elif(path[5]  == "Nigeria"):
            node1_y = 8.648911
            node1_x = 7.907745      
        elif(path[5]  == "United Kingdom"):
            node1_y = 53.108865
            node1_x = -1.402979
        elif(path[5] == "Algeria"):
            node1_y = 28.033886
            node1_x = 1.659626
        elif(path[5] == "Egypt"):
            node1_y = 27.024681
            node1_x = 28.802349             
            
        # Converting x and y to latitude and longitude
        mx,my = m(node1_x,node1_y)
            
        if(path[6]  == "South Africa"):
            node2_y = -29.16895
            node2_x = 26.568181
        elif(path[6] == "Zimbabwe"):
            node2_y = -19.329287
            node2_x = 30.170774
        elif(path[6] == "Congo"):
            node2_y = -2.479389
            node2_x = 23.987360
        elif(path[6] == "Mozambique"):
            node2_y = -18.164121
            node2_x = 35.673637
        elif(path[6] == "Botswana"):
            node2_y = -22.773649
            node2_x = 24.075226
        elif(path[6] == "Malawi"):
            node2_y = -13.856747
            node2_x = 34.092036  
        elif(path[6] == "Nigeria"):
            node2_y = 8.648911
            node2_x = 7.907745      
        elif(path[6] == "United Kingdom"):
            node2_y = 53.108865
            node2_x = -1.402979
        elif(path[6] == "Algeria"):
            node1_y = 28.033886
            node1_x = 1.659626
        elif(path[6] == "Egypt"):
            node1_y = 27.024681
            node1_x = 28.802349              
        
        # Converting x and y to latitude and longitude 
        mx2,my2 = m(node2_x,node2_y)
        
        # Adding nodes, edge and weight to the graph 
        G.add_node(node1, pos = (mx,my), color = col)
        G.add_node(node2, pos = (mx2,my2), color = col2)
        G.add_edge(node1, node2, weight = weight_user)
        
        pos1 = node1_x + 5.013474
        pos2 = node2_x + 5.013474
        pos3 = pos3 + 5.013474;
        
        
    file.close
      
    # To show weights on graph interface
    weight = nx.get_edge_attributes(G, 'weight')  
    pos = nx.get_node_attributes(G, 'pos')
    
    # Statement used to draw the graph and show node labels
    nx.draw(G, pos, with_labels = True)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_one, node_color='r', node_shape='o', node_size=1000)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_two, node_color='g', node_shape='s', node_size=500)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_three, node_shape = 'o', node_color='purple')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels = weight)
        
    m.drawcountries(linewidth = 1)
    m.drawstates(linewidth = 0.2)
    m.drawcoastlines(linewidth=1)
    plt.title("Network Provided to African countries by ISP's.")
     
    # m.shaderelief()
    plt.tight_layout()
    
    plt.show() 
    

#deleting a node from the graph
def delete_node():
    #pass
    plt.clf()
    node = pyautogui.prompt("Enter the node you want to delete")
    file = open("nodes.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("nodes.txt","w")
    for line in lines:
        found = False
        path = line.split(",")
        if node == path[0]:
            found = True
        if node == path[1]:
            found= True
        if found == False:
            file.write(line)
            #file.write("check")
    
    file.close()
    G.remove_node(int(node))
    draw_graph()
v = StringVar()

def show_shortest_path():
    
    # To show a dialog with radio buttons for algorithm options
    dialogb = Tk()
    dialogb.title("")
    dialogb.geometry("150x100")
    
    Label(dialogb, text = "Select an algorithm").grid(row = 0, column = 0, sticky = W )
    radio_button1 = Radiobutton(dialogb, text = "Dijkstra Algorith", variable = v, value = "1", command = calc_dijskra)
    radio_button1.grid(row = 1, column = 0, sticky = W )
    radio_button2 = Radiobutton(dialogb, text = "Bellman Ford Algorith", variable = v, value = "2", command = calc_bellman)
    radio_button2.grid(row = 2, column = 0, sticky = W )
    

def calc_bellman():
    
    
    
    source_node = pyautogui.prompt("Enter source node")
    dest_node = pyautogui.prompt("Enter destination node")
    pos = nx.get_node_attributes(G, 'pos')
    path = nx.shortest_path(G, source = int(source_node) , target = int(dest_node))
    path_edges = zip(path,path[1:])
    path_edges = set(path_edges)
    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
    plt.axis('equal')
    #ani = animation.FuncAnimation(fig, update, frames=6, interval=1000, repeat=True)
    plt.ion()
    plt.draw()
    plt.show()

def calc_dijskra():
    
    no_of_packets = pyautogui.prompt("How many packets do you want to send?")
    source_and_dest_nodes = pyautogui.prompt("Enter source and destination nodes seperated by a comma")
    array_nodes = source_and_dest_nodes.split(",")
    
    arr_colors = ['r','b','g','r','b','g']
    arr_edges = ['solid','dashed','dotted','dashdot']
    y = 0
    for x in range(int(no_of_packets)):
        
        pos = nx.get_node_attributes(G, 'pos')
        path = nx.shortest_path(G, source = int(array_nodes[0]) , target = int(array_nodes[1]))
        path_edges = zip(path,path[1:])
        path_edges = set(path_edges)
        if y > 5:
            y = 0
        nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
        nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color=arr_colors[y],width=10, style = arr_edges[random.randint(0,3)])
        y = y + 1
        plt.axis('equal')
        #ani = animation.FuncAnimation(fig, update, frames=6, interval=1000, repeat=True)
        plt.ion()
        plt.draw()
        plt.show()
        
        #draw_graph()
        #draw_graph()
        plt.pause(1)

# used to prompt the user if they want to exit, also delete all the nodes in the text file.    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        file = open("nodes.txt","w")
        file.close()
        sys.exit(0)
        root.destroy()

def import_cvs():
    
    filename = pyautogui.prompt("Enter the name/location of the CSV file.")    
    
    # denoting that these are globally institiated
    global pos1
    global pos2
    global pos3
    
    global var
    global var2
        
    # color map to maap different color for each node in a particular tier
    color_map = []
    
    t_one = []
    t_two = []
    t_three = []
    
    
    # reading from the nodes.txt file
    file = open(filename+".txt", "r")
    for line in file:
        path = line.split(",")
        
        # Get Nodes and Weight
        node1 = int(path[0])
        node2 = int(path[1])
        weight_user = path[2]
        
        # Assign colors to nodes, nodes in T1 = Red, T2 = Green, T3 = blue
        col = ''
        col2 = ''
        
        # Note on the UI x ranges from 0.971534 to 1.01547 & y ranges from 1.85451 to 2.01905
        
        # Getting the tier so i can display node in a suitable position in Graph interface
        node1_tier = int(path[3])
        node2_tier = int(path[4])
        
        if node1_tier == 1:           
            col = 'red'
            if node1 not in t_one:
                t_one.append(node1)
            
        elif node1_tier == 2:            
            col = 'green'
            if node1 not in t_two:
                t_two.append(node1)            
                        
        else:  
            col = 'blue'
            if node1 not in t_three:
                t_three.append(node1)            
        
        if node2_tier == 1:            
            col2 = 'red'
            if node2 not in t_one:
                t_one.append(node2)            
                       
        elif node2_tier == 2:            
            col2 = 'green'
            if node2 not in t_two:
                t_two.append(node2)             
                       
        else:
            col2 = 'blue'
            if node2 not in t_three:
                t_three.append(node2)             

        if(path[5] == "South Africa"):
            node1_y = -29.16895
            node1_x = 26.568181
        elif(path[5] == "Zimbabwe"):
            node1_y = -19.329287
            node1_x = 30.170774
        elif(path[5]  == "Congo"):
            node1_y = -2.479389
            node1_x = 23.987360
        elif(path[5]  == "Mozambique"):
            node1_y = -18.164121
            node1_x = 35.673637
        elif(path[5]  == "Botswana"):
            node1_y = -22.773649
            node1_x = 24.075226
        elif(path[5]  == "Malawi"):
            node1_y = -13.856747
            node1_x = 34.092036  
        elif(path[5]  == "Nigeria"):
            node1_y = 8.648911
            node1_x = 7.907745      
        elif(path[5]  == "United Kingdom"):
            node1_y = 53.108865
            node1_x = -1.402979
        elif(path[5] == "Algeria"):
            node1_y = 28.033886
            node1_x = 1.659626
        elif(path[5] == "Egypt"):
            node1_y = 27.024681
            node1_x = 28.802349             
            
        # Converting x and y to latitude and longitude
        mx,my = m(node1_x,node1_y)
            
        if(path[6]  == "South Africa"):
            node2_y = -29.16895
            node2_x = 26.568181
        elif(path[6] == "Zimbabwe"):
            node2_y = -19.329287
            node2_x = 30.170774
        elif(path[6] == "Congo"):
            node2_y = -2.479389
            node2_x = 23.987360
        elif(path[6] == "Mozambique"):
            node2_y = -18.164121
            node2_x = 35.673637
        elif(path[6] == "Botswana"):
            node2_y = -22.773649
            node2_x = 24.075226
        elif(path[6] == "Malawi"):
            node2_y = -13.856747
            node2_x = 34.092036  
        elif(path[6] == "Nigeria"):
            node2_y = 8.648911
            node2_x = 7.907745      
        elif(path[6] == "United Kingdom"):
            node2_y = 53.108865
            node2_x = -1.402979
        elif(path[6] == "Algeria"):
            node1_y = 28.033886
            node1_x = 1.659626
        elif(path[6] == "Egypt"):
            node1_y = 27.024681
            node1_x = 28.802349              
        
        # Converting x and y to latitude and longitude 
        mx2,my2 = m(node2_x,node2_y)
        
        # Adding nodes, edge and weight to the graph 
        G.add_node(node1, pos = (mx,my), color = col)
        G.add_node(node2, pos = (mx2,my2), color = col2)
        G.add_edge(node1, node2, weight = weight_user)
        
        pos1 = node1_x + 5.013474
        pos2 = node2_x + 5.013474
        pos3 = pos3 + 5.013474;
        
        
    file.close
      
    # To show weights on graph interface
    weight = nx.get_edge_attributes(G, 'weight')  
    pos = nx.get_node_attributes(G, 'pos')
    
    # Statement used to draw the graph and show node labels
    nx.draw(G, pos, with_labels = True)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_one, node_color='r', node_shape='o', node_size=1000)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_two, node_color='g', node_shape='s', node_size=500)
    nx.draw_networkx_nodes(G, pos, with_labels = True, nodelist = t_three, node_shape = 'o', node_color='purple')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels = weight)
        
    m.drawcountries(linewidth = 1)
    m.drawstates(linewidth = 0.2)
    m.drawcoastlines(linewidth=1)
    plt.title("Network Provided to African countries by ISP's.")
     
    # m.shaderelief()
    plt.tight_layout()
    
    plt.show()    
    
def export_cvs():
    #pass
    filename = pyautogui.prompt("Enter the name you would like to save file as:")
    with open("nodes.txt") as f:
        with open(filename+".txt", "w") as f1:
            for line in f:
                f1.write(line)     


# End of Functions --------------------------------------------------------------------------------------------------------



#Label to display header
Label(main, text = "  --------------  Inter-domain Routing Simulator  --------------", fg = 'blue', bg = 'black').grid(row = 0, column = 0, sticky = N)
Label(main, text = "", bg = 'black').grid(row = 1, column = 0, sticky = N)


# (Start) Frame to put my widgets in ---------------------------------------------------------------------------------------
Frame_one = Frame(main, bg = 'black')
Frame_one.grid(row = 2, column = 0, sticky = W)

# I will add labels and input fields on my Frame

# For Node 1
Label(Frame_one, text = "Enter Node 1 Label: ", fg = 'white', bg = 'black').grid(row = 0, column = 0, sticky = W)
node1_input_box = Entry(Frame_one, width = 10, )
node1_input_box.grid(row = 0, column = 1, sticky = W)

# For Node 2
Label(Frame_one, text = "Enter Node 2 label: ", fg = 'white', bg = 'black').grid(row = 1, column = 0, sticky = W)
node2_input_box = Entry(Frame_one, width = 10)
node2_input_box.grid(row = 1, column = 1, sticky = W)

# For Weight
Label(Frame_one, text = "Edge weight between Node 1 & Node 2: ", fg = 'white', bg = 'black').grid(row = 3, column = 0, sticky = W)
# weight_input_box = Entry(Frame_one, width = 5)
weight_spinner = Spinbox(Frame_one, from_ = 0, to  = 100, width = 5)
weight_spinner.grid(row = 3, column = 1, sticky = W)
# weight_input_box.grid(row = 3, column = 1, sticky = W)
Label(main, text = "", bg = 'black').grid(row = 4, column = 0, sticky = N)

# End of Frame 1 -------------------------------------------------------------------------------------------------------

# Start of frame 2 -----------------------------------------------------------------------------------------------------
Frame_two = Frame(main, bg = 'black')
Frame_two.grid(row = 5, column = 0, sticky = W)

var = StringVar(main)
var.set("South Africa") # initial value

var2 = StringVar(main)
var2.set("South Africa") # initial value

var3 = StringVar(main)
var3.set("1") # initial value

var4 = StringVar(main)
var4.set("1") # initial value

# Input For Tier 1 valuez
Label(Frame_two, text = " Enter Tier No. for Node 1: ", fg = 'white', bg = 'black').grid(row = 0, column = 0, sticky = W)
# tier1_input_box = Entry(Frame_two, width = 5)
# tier1_input_box.grid(row = 0, column = 1, sticky = W)
option3 = OptionMenu(Frame_two, var3, "1","2","3")
option3.grid(row = 0, column = 1, padx=(10, 10))
option = OptionMenu(Frame_two, var, "South Africa", "Zimbabwe", "United Kingdom", "Mozambique", "USA", "Malawi", "Algeria", "Nigeria", "Congo", "Egypt")
option.grid(row = 0, column = 2, padx=(10, 10))

# Input For Tier 2 value
Label(Frame_two, text = " Enter Tier No. for Node 2: ", fg = 'white', bg = 'black').grid(row = 1, column = 0, pady=(10,10))
# tier2_input_box = Entry(Frame_two, width = 5)
# tier2_input_box.grid(row = 1, column = 1, sticky = W)
option4 = OptionMenu(Frame_two, var4, "1","2","3")
option4.grid(row = 1, column = 1, padx=(10, 10))
option2 = OptionMenu(Frame_two, var2, "South Africa", "Zimbabwe", "United Kingdom", "Mozambique", "USA", "Malawi", "Algeria", "Nigeria", "Congo", "Egypt")
option2.grid(row = 1, column = 2, padx=(10, 10))

Label(Frame_two, text = "", bg = 'black').grid(row = 3, column = 0, sticky = W)
# End of frame 2 -------------------------------------------------------------------------------------------------------


# Start of frame 3 -----------------------------------------------------------------------------------------------------
Frame_three = Frame(main, bg = 'black')
Frame_three.grid(row = 6, column = 0, sticky = W)
Label(Frame_three, text = "   ---------------  ", fg = 'blue', bg = 'black').grid(row = 0, column = 0, sticky = W)

# Button to write nodes,edges,weights into a file
Button(Frame_three, text = "Deploy Nodes", width = 20, command = deploy_nodes).grid(row = 0, column = 1, sticky = W)
Label(Frame_three, text = "  ----------------", fg = 'blue', bg = 'black').grid(row = 0, column = 2, sticky = W)

Label(Frame_three, text = "", bg = 'black').grid(row = 1, column = 0, sticky = N)

# Button to invoke the graph display interface
Label(Frame_three, text = "   ---------------  ", fg = 'blue', bg = 'black').grid(row = 2, column = 0, sticky = W)
Button(Frame_three, text = "Show Graph", width = 20, command = draw_graph).grid(row = 2, column = 1, sticky = W)
Label(Frame_three, text = "  ----------------", fg = 'blue', bg = 'black').grid(row = 2, column = 2, sticky = W)

Label(Frame_three, text = "", bg = 'black').grid(row = 3, column = 0, sticky = N)

# Show path from node a to node b
Label(Frame_three, text = "   ---------------  ", fg = 'blue', bg = 'black').grid(row = 4, column = 0, sticky = W)
Button(Frame_three, text = "Show Shortest Path", width = 20, command = show_shortest_path ).grid(row = 4, column = 1, sticky = W)
Label(Frame_three, text = "  ----------------", fg = 'blue', bg = 'black').grid(row = 4, column = 2, sticky = W)

Label(Frame_three, text = "", bg = 'black').grid(row = 5, column = 0, sticky = N)

# Delete Node Button
Label(Frame_three, text = "   ---------------  ", fg = 'blue', bg = 'black').grid(row = 6, column = 0, sticky = W)
Button(Frame_three, text = "Delete Node", width = 20, command = delete_node ).grid(row = 6, column = 1, sticky = W)
Label(Frame_three, text = "  ----------------", fg = 'blue', bg = 'black').grid(row = 6, column = 2, sticky = W)

# End of frame three ----------------------------------------------------------------------------------------------------

Label(main, text = "", bg = 'black').grid(row = 7, column = 0, sticky = N)

# Start of frame four ----------------------------------------------------------------------------------------------------

Frame_four = Frame(main, bg = 'black')
Frame_four.grid(row = 8, column = 0, sticky = W)
Label(Frame_four, text = " --", fg = 'blue', bg = 'black').grid(row = 0, column = 0, sticky = W)
Button(Frame_four, text = "Import CSV", width = 20, command = import_cvs).grid(row = 0, column = 1, sticky = W)
Button(Frame_four, text = "Export CSV", width = 20, command = export_cvs).grid(row = 0, column = 2, sticky = W)
Label(Frame_four, text = "--", fg = 'blue', bg = 'black').grid(row = 0, column = 3, sticky = W)

# End of frame four --------------------------------------------------------------------------------------------------------

# Interaction between the application and the window manager, this provides definition on what occurs when a user excplicitly exit a wibdow using window manager
main.protocol("WM_DELETE_WINDOW", on_closing)

# Display my GUI
main.mainloop()