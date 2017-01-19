def maskHideAll():
    layer = mari.geo.current().currentChannel().currentLayer()

    if layer.hasMask() == True:
        pass

    else:

        mask = layer.makeMask()

        imageSet = mask.imageList()

        black = mari.Color(0, 0, 0, 0)

        for image in imageSet:
            image.fill(black)

