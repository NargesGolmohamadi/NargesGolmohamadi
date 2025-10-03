#include "BulletEnemy.h"
#include "Game.h"
#include "Enemy.h"
#include <QTimer>
#include <QGraphicsScene>
#include <QList>
#include <QGraphicsPixmapItem>


extern Game *game; // there is an external global object called game

BulletEnemy::BulletEnemy(QGraphicsItem *parent): QObject(),QGraphicsPixmapItem(parent){
    //drew graphics
    setPixmap(QPixmap(":/photos/bullet.png"));


    //connect
    QTimer *timer = new QTimer();
    connect(timer, SIGNAL(timeout()),this,SLOT(move()));

    timer->start(50);
}

void BulletEnemy::move()
{   // if bullet collides with enemy , destroy both
    QList <QGraphicsItem *> colliding_items = collidingItems();
    for ( int i =0 , n = colliding_items.size(); i < n; i++){
        if(typeid(* (colliding_items[i]))== typeid(Player)){
            //increase the score
            game->health->decrease();

            //remove bullet both
            scene()->removeItem(this); //bullet
            delete this;
            if(game->health->getHealth()==0){
                game->endGame(QString("GAME OVER!"));
            }
            return;
        }

    }


    setPos(x(),y()+10);
    // if the bullet is off the screen, destroy it
    if (pos().y() < 0){
        scene()->removeItem(this);
        delete this;
    }
}
