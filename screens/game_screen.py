import math

import pygame
import settings as cfg
from game.entities import Paddle, Ball


def run(screen: pygame.Surface, clock: pygame.time.Clock, level: int) -> None:
    paddle = Paddle()

    keys = pygame.key.get_pressed()
    paddle.move(keys)

    paddle.draw(screen)


def _resize_paddle(paddle: Paddle, new_width: int) -> None:
    """ Resizes the Paddle around its center, keeping it inside the field. """
    center = paddle.rect.centerx
    new_width = max(cfg.PADDLE_MIN_WIDTH, min(cfg.PADDLE_MAX_WIDTH, new_width))
    paddle.rect.width = new_width
    paddle.rect.centerx = center

    if paddle.rect.left < cfg.FIELD_LEFT:
        paddle.rect.left = cfg.FIELD_LEFT
    if paddle.rect.right > cfg.FIELD_RIGHT:
        paddle.rect.right = cfg.FIELD_RIGHT


def _scale_ball_speed(ball: Ball, factor: float) -> None:
    """ Scales a Ball's velocity vector, clamped to min/max speed. """
    speed = math.hypot(ball.vx, ball.vy)
    new_speed = max(cfg.MIN_BALL_SPEED, min(cfg.MAX_BALL_SPEED, speed * factor))
    if speed == 0:
        return
    scale = new_speed / speed
    ball.vx *= scale
    ball.vy *= scale


def apply_bonus(bonus_type: str, paddle: Paddle, balls: list[Ball], state: dict) -> None:

    if bonus_type == "extend":
        _resize_paddle(paddle, paddle.rect.width + cfg.PADDLE_EXTEND_STEP)

    elif bonus_type == "shrink":
        _resize_paddle(paddle, paddle.rect.width - cfg.PADDLE_SHRINK_STEP)

    elif bonus_type == "speed_up":
        for ball in balls:
            _scale_ball_speed(ball, cfg.BALL_SPEED_FACTOR)

    elif bonus_type == "speed_down":
        for ball in balls:
            _scale_ball_speed(ball, 1 / cfg.BALL_SPEED_FACTOR)

    elif bonus_type == "multiball":
        for ball in balls[:]:
            clone = Ball(ball.rect.centerx, ball.rect.centery)
            clone.vx, clone.vy = -ball.vx, ball.vy
            balls.append(clone)

    elif bonus_type == "laser":
        paddle.laser = True

    elif bonus_type == "extra_life":
        state["lives"] = state.get("lives", 3) + 1