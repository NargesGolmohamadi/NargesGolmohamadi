#ifndef PLAYER_H
#define PLAYER_H

#include <QGraphicsPixmapItem>
#include <QGraphicsItem>

class Player :public QGraphicsPixmapItem{
public:
    Player (QGraphicsItem *parent=0);
    void keyPressEvent(QKeyEvent *event);
};



#endif // PLAYER_H
