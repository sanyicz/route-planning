import tkinter as tk
import numpy as np

class RoutePlanningSimulator(object):
    def __init__(self, window, canvasSize=(500, 500), gridSize=(10, 10)):
        self.window = window
        self.window.columnconfigure(0, weight=1)
        self.canvasSize = canvasSize
        self.gridSize = gridSize
        self.fieldArray = np.zeros(self.gridSize, dtype=int)
        
        self.buttonsFrame = tk.Frame(self.window)
        self.buttonsFrame.grid(row=0, column=0)

        self.fieldFrame = tk.Frame(self.window)
        self.fieldFrame.grid(row=1, column=0)
        self.fieldFrame.columnconfigure(0, weight=1)
        
        self.W, self.H = canvasSize[0], canvasSize[0]
        self.w, self.h = gridSize[0], gridSize[0]
        self.gridDelta = max(self.canvasSize) // max(self.gridSize)
        self.fieldCanvas = tk.Canvas(self.fieldFrame, width=self.W, height=self.H, background='white', borderwidth=0, highlightthickness=0)
        self.fieldCanvas.grid(row=0, column=0)
        
        self.main()

    def main(self):
        #delete or empty widgets
        for child in self.buttonsFrame.winfo_children():
            child.destroy()
        #create and configure widgets
        self.commandButton = tk.Button(self.buttonsFrame, text='Finish grid', command=self.finishGrid)
        self.commandButton.grid(row=0, column=0)
        for i in range(self.w):
            for j in range(self.h):
                self.fieldCanvas.create_rectangle(i*self.gridDelta, j*self.gridDelta, (i+1)*self.gridDelta, (j+1)*self.gridDelta)
        self.fieldCanvas.bind('<ButtonPress-1>', self.setGrid)
        self.startPosition, self.endPosition = None, None

    def setGrid(self, event):
        x, y = event.x, event.y #left mouse click coordinates in pixel
        x, y = x // self.gridDelta, y // self.gridDelta #grid position
        #set the positon (x, y) in the array that represents the field to 1 if it is 0
        self.fieldArray[y][x] = 1 if self.fieldArray[y][x] == 0 else 0
        print(self.fieldArray)
        #draw a black rectangle if the position was empty, white otherwise
        if self.fieldArray[y][x] == 1:
            self.fieldCanvas.create_rectangle(x*self.gridDelta, y*self.gridDelta, (x+1)*self.gridDelta, (y+1)*self.gridDelta, fill='black')
        else:
            self.fieldCanvas.create_rectangle(x*self.gridDelta, y*self.gridDelta, (x+1)*self.gridDelta, (y+1)*self.gridDelta, fill='white')

    def finishGrid(self):
        self.commandButton.config(text='Plan route', command=self.planRoute)
        self.fieldCanvas.bind('<ButtonPress-1>', self.setStartPosition)
        self.fieldCanvas.bind('<ButtonPress-3>', self.setEndPosition)

    def setStartPosition(self, event):
        x, y = event.x, event.y #left mouse click coordinates in pixel
        x, y = x // self.gridDelta, y // self.gridDelta #grid position
        if self.fieldArray[y][x] == 0:
            #clear previous position
            if self.startPosition != None:
                i, j = self.startPosition
                self.fieldCanvas.create_rectangle(i*self.gridDelta, j*self.gridDelta, (i+1)*self.gridDelta, (j+1)*self.gridDelta, fill='white')
            #draw new position
            self.fieldCanvas.create_rectangle(x*self.gridDelta, y*self.gridDelta, (x+1)*self.gridDelta, (y+1)*self.gridDelta, fill='blue')
            self.startPosition = (x, y)
            print(f'self.startPosition: {self.startPosition}')
        else: #invalid position: a wall is selected
            pass

    def setEndPosition(self, event):
        x, y = event.x, event.y #right mouse click coordinates in pixel
        x, y = x // self.gridDelta, y // self.gridDelta #grid position
        if self.fieldArray[y][x] == 0:
            #clear previous position
            if self.endPosition != None:
                i, j = self.endPosition
                self.fieldCanvas.create_rectangle(i*self.gridDelta, j*self.gridDelta, (i+1)*self.gridDelta, (j+1)*self.gridDelta, fill='white')
            #draw new position
            self.fieldCanvas.create_rectangle(x*self.gridDelta, y*self.gridDelta, (x+1)*self.gridDelta, (y+1)*self.gridDelta, fill='red')
            self.endPosition = (x, y)
            print(f'self.endPosition: {self.endPosition}')
        else: #invalid position: a wall is selected
            pass

    def planRoute(self):
        #if start or end is not selected, select randomly
        pass

    def quit(self):
        self.window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
##    screen_width = window.winfo_screenwidth()
##    screen_height = window.winfo_screenheight()
##    screen_width, screen_height = 500, 500
##    window.geometry(str(screen_width) + 'x' + str(screen_height))
##    window.update_idletasks() #with this window.winfo_width() returns the correct value
    RPS = RoutePlanningSimulator(window)
    window.mainloop()
