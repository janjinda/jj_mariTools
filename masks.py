import mari
import os


def maskHideAll():
    layer = mari.geo.current().currentChannel().currentLayer()

    if layer.hasMask():
        pass

    else:

        mask = layer.makeMask()

        imageSet = mask.imageList()

        black = mari.Color(0, 0, 0, 0)

        for image in imageSet:
            image.fill(black)


maskHideAllAction = mari.actions.create("jj_mariTools/Mask Hide All", "masks.maskHideAll()")

icon_filename = 'Hide.png'
icon_path = mari.resources.path(mari.resources.ICONS) + os.sep +  icon_filename
maskHideAllAction.setIconPath(icon_path)
maskHideAllAction.setIconPath(icon_path)