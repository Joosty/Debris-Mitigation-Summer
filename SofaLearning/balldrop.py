import Sofa.Core

# Required import for python
import Sofa


# Choose in your script to activate or not the GUI
USE_GUI = True


def main():
    # Call the SOFA function to create the root node
    root = Sofa.Core.Node("root")

    # Call the createScene function, as runSofa does
    createScene(root)

    # Once defined, initialization of the scene graph
    Sofa.Simulation.init(root)

    # Launch the GUI (qt or qglviewer)
    Sofa.Gui.GUIManager.Init("myscene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root, __file__)
    Sofa.Gui.GUIManager.SetDimension(1080, 800)

    # Initialization of the scene will be done here
    Sofa.Gui.GUIManager.MainLoop(root)
    Sofa.Gui.GUIManager.closeGUI()



# Function used only if this script is called from a python environment
if __name__ == '__main__':
    main()

def createScene(rootNode):
        rootNode.addObject("VisualGrid", nbSubdiv=10, size=1000)

        confignode = rootNode.addChild("Config")
        confignode.addObject('OglSceneFrame', style="Arrows", alignment="TopRight")


        # Creating the falling sphere object
        sphere = rootNode.addChild("sphere")
        sphere.addObject('MechanicalObject', name="mstate", template="Rigid3", translation2=[0., 0., 0.], rotation2=[0., 0., 0.], showObjectScale=50)

        #### Visualization subnode for the sphere
        sphereVisu = sphere.addChild("VisualModel")
        sphereVisu.loader = sphereVisu.addObject('MeshOBJLoader', name="loader", filename="mesh/ball.obj")
        sphereVisu.addObject('OglModel', name="model", src="@loader", scale3d=[50]*3, color=[0., 1., 0.], updateNormals=False)
        sphereVisu.addObject('RigidMapping')

        return rootNode

if __name__ == '__main__':
    main()