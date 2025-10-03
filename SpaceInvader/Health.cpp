#include "Health.h"
#include <QFont>

Health::Health(QGraphicsItem *parent): QGraphicsTextItem(parent)
{
    //intialize the health to 3
    health = 3;

    //draw the text
    setPlainText(QString("Health: ")+ QString :: number(health)); //score : 0
    setDefaultTextColor(Qt::darkGreen);
    setFont(QFont("times",16));
}

void Health::decrease()
{
    health --;
    setPlainText(QString("Health: ")+ QString :: number(health));
}

int Health::getHealth(){
    return health;
}

