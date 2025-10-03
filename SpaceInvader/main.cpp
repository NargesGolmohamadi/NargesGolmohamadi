#include <QApplication>
#include "Game.h"

Game *game;


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    game = new Game();
    game->show();
    game->displayMenu(QString ("SPACE INVADOR"));

    return a.exec();
}
