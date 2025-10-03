#ifndef ENEMY_H
#define ENEMY_H

#include <QGraphicsPixmapItem>
#include <QObject>
#include <QGraphicsItem>

class Enemy :public QObject, public QGraphicsPixmapItem {
    Q_OBJECT
private:
    int type;
public:
    Enemy(QGraphicsItem *parent=0);

public slots:
    void shoot();
};

#endif // ENEMY_H
