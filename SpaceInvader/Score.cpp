#include "Score.h"
#include <QFont>

Score::Score(QGraphicsItem *parent): QGraphicsTextItem(parent)
{
    //intialize the score to 0
    score = 0;

    //draw the text
    setPlainText(QString("Score: ")+ QString :: number(score)); //score : 0
    setDefaultTextColor(Qt::darkGreen);
    setFont(QFont("times",16));
}

void Score::increase()
{
    score ++;
    setPlainText(QString("Score: ")+ QString :: number(score));
}

int Score::getScore(){
    return score;
}

