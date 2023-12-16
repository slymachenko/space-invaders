class Updater:
    def update(self, *nodes) -> None:
        for node in nodes:
            node.update()