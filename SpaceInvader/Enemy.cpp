#include "Enemy.h"
#include <QTimer>
#include <QGraphicsScene>
#include <QList>
#include <stdlib.h>
#include "Game.h"
#include <QRandomGenerator>
#include "BulletEnemy.h"

extern Game *game;

#include <QDebug>
Enemy::Enemy(QGraphicsItem *parent):QObject(), QGraphicsPixmapItem(parent){

    this->type = QRandomGenerator::global()->generate()%3+1;
    if (type ==1 ){
        setPixmap(QPixmap(":/photos/Enemy.png"));
        setTransformOriginPoint(50,50);
    }
    else if (type==2){
        setPixmap(QPixmap(":/photos/6.png"));
        setTransformOriginPoint(50,50);
        QTimer *timer = new QTimer();
        connect(timer, SIGNAL(timeout()),this,SLOT(shoot()));
        timer->start(6000);
    }
    else if (type==3){
        setPixmap(QPixmap(":/photos/9.png"));
        setTransformOriginPoint(50,50);
        QTimer *timer = new QTimer();
        connect(timer, SIGNAL(timeout()),this,SLOT(shoot()));
        timer->start(10000);
    }

}


void Enemy::shoot()
{
    BulletEnemy *bullet_enemy = new BulletEnemy();
    bullet_enemy->setPos(x()+19.5,y()+27);
    scene()->addItem(bullet_enemy);

}
