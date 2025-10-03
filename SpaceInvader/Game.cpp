#include "Game.h"
#include "Enemy.h"
#include <QTimer>
#include <QGraphicsTextItem>
#include <QFont>

Game::Game(QWidget *parent)
{
    // creat a scene
    scene = new QGraphicsScene();
    scene->setSceneRect(0,0,800,600);
    setBackgroundBrush(QBrush(QImage(":/photos/background.png")));

    //make the newly created scene the scene to visualize
    setScene(scene);
    setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    setFixedSize(800,600);

}

void Game::displayMenu(QString text)
{
    // create the title text
    QGraphicsTextItem* titleText = new QGraphicsTextItem(text);
    QFont titleFont("comic sans",50);
    titleText->setFont(titleFont);
    int txPos = this->width()/2 - titleText->boundingRect().width()/2;
    int tyPos = 150;
    titleText->setPos(txPos,tyPos);
    scene->addItem(titleText);

    // create the play button
    Button* playButton = new Button(QString("Play"));
    int bxPos = this->width()/2 - playButton->boundingRect().width()/2;
    int byPos = 275;
    playButton->setPos(bxPos,byPos);
    connect(playButton,SIGNAL(clicked()),this,SLOT(start()));
    scene->addItem(playButton);

    // create the quit button
    Button* quitButton = new Button(QString("Quit"));
    int qxPos = this->width()/2 - quitButton->boundingRect().width()/2;
    int qyPos = 350;
    quitButton->setPos(qxPos,qyPos);
    connect(quitButton,SIGNAL(clicked()),this,SLOT(close()));
    scene->addItem(quitButton);
}

void Game::endGame(QString text)
{
    scene->clear();
    displayMenu(text);
}

void Game::start()
{
    scene->clear();
    // create the player
    player = new Player();
    player->setPos(400,500);

    //make the player focusable and set it to be the current focus
    player->setFlag(QGraphicsRectItem::ItemIsFocusable);
    player->setFocus();

    // add player to the scene
    scene->addItem(player);

    //creat the score
    score = new Score();
    scene->addItem(score);

    //creat the health
    health = new Health();
    health->setPos(health->x(),health->y()+25);
    scene->addItem(health);

    //create the enemies

    Enemy *enemy1 = new Enemy();
    enemy1->setPos(80,30);
    scene->addItem(enemy1);

    Enemy *enemy2 = new Enemy();
    enemy2->setPos(145,30);
    scene->addItem(enemy2);

    Enemy *enemy3 = new Enemy();
    enemy3->setPos(210,30);
    scene->addItem(enemy3);

    Enemy *enemy4 = new Enemy();
    enemy4->setPos(275,30);
    scene->addItem(enemy4);

    Enemy *enemy5 = new Enemy();
    enemy5->setPos(340,30);
    scene->addItem(enemy5);

    Enemy *enemy6 = new Enemy();
    enemy6->setPos(405,30);
    scene->addItem(enemy6);

    Enemy *enemy7 = new Enemy();
    enemy7->setPos(470,30);
    scene->addItem(enemy7);

    Enemy *enemy8 = new Enemy();
    enemy8->setPos(535,30);
    scene->addItem(enemy8);


    Enemy *enemy9 = new Enemy();
    enemy9->setPos(600,30);
    scene->addItem(enemy9);

    Enemy *enemy10 = new Enemy();
    enemy10->setPos(665,30);
    scene->addItem(enemy10);


    Enemy *enemy11 = new Enemy();
    enemy11->setPos(80,100);
    scene->addItem(enemy11);

    Enemy *enemy12 = new Enemy();
    enemy12->setPos(145,100);
    scene->addItem(enemy12);

    Enemy *enemy13 = new Enemy();
    enemy13->setPos(210,100);
    scene->addItem(enemy13);

    Enemy *enemy14 = new Enemy();
    enemy14->setPos(275,100);
    scene->addItem(enemy14);

    Enemy *enemy15 = new Enemy();
    enemy15->setPos(340,100);
    scene->addItem(enemy15);

    Enemy *enemy16 = new Enemy();
    enemy16->setPos(405,100);
    scene->addItem(enemy16);

    Enemy *enemy17 = new Enemy();
    enemy17->setPos(470,100);
    scene->addItem(enemy17);

    Enemy *enemy18 = new Enemy();
    enemy18->setPos(535,100);
    scene->addItem(enemy18);


    Enemy *enemy19 = new Enemy();
    enemy19->setPos(600,100);
    scene->addItem(enemy19);

    Enemy *enemy20 = new Enemy();
    enemy20->setPos(665,100);
    scene->addItem(enemy20);



    show();

}
