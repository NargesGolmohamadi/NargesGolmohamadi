#ifndef GAME_H
#define GAME_H

#include <QGraphicsView>
#include <QWidget>
#include <QGraphicsScene>
#include "Player.h"
#include "Score.h"
#include "Health.h"
#include "Button.h"

class Game: public QGraphicsView{
    Q_OBJECT

public:
    Game(QWidget *parent=0);
    void displayMenu(QString text);
    void endGame(QString text);
    QGraphicsScene *scene;
    Player *player;
    Score *score;
    Health *health;
public slots:
    void start();

};

#endif // GAME_H
