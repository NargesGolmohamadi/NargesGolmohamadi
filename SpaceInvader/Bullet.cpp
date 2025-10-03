#include "Bullet.h"
#include "Game.h"
#include "Enemy.h"
#include <QTimer>
#include <QGraphicsScene>
#include <QList>
#include <QGraphicsPixmapItem>


extern Game *game; // there is an external global object called game

Bullet::Bullet(QGraphicsItem *parent): QObject(),QGraphicsPixmapItem(parent){
    //drew graphics
    setPixmap(QPixmap(":/photos/bullet.png"));


    //connect
    QTimer *timer = new QTimer();
    connect(timer, SIGNAL(timeout()),this,SLOT(move()));
    timer->start(50);
}

void Bullet::move()
{   // if bullet collides with enemy , destroy both
    QList <QGraphicsItem *> colliding_items = collidingItems();
    for ( int i =0 , n = colliding_items.size(); i < n; i++){
        if(typeid(* (colliding_items[i]))== typeid(Enemy)){
            //increase the score
            game->score->increase();

            //remove them both
            scene()->removeItem(colliding_items[i]);//enemy
            scene()->removeItem(this); //bullet
            delete colliding_items[i];
            delete this;
            if(game->score->getScore()==20){
                game->endGame(QString("WINNER!"));
            }
            return;
        }

    }


    setPos(x(),y()-10);
    // if the bullet is off the screen, destroy it
    if (pos().y() < 0){
        scene()->removeItem(this);
        delete this;
    }
}
