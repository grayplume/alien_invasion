import pygame


class Hutao():
    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/hutao.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)
