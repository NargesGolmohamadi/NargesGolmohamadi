#ifndef BULLETENEMY_H
#define BULLETENEMY_H

#include <QGraphicsPixmapItem>
#include <QGraphicsItem>
#include <QObject>

class BulletEnemy :public QObject, public QGraphicsPixmapItem {
    Q_OBJECT
public:
    BulletEnemy(QGraphicsItem *parent=0);

public slots:
    void move();
};

#endif // BULLETENEMY_H
