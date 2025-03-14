from code.Background import Background
from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Collision import Collision
from code.Score import Score


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:  # Verificando se saiu pelo fundo

                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2, entity_list, sprite_group):
        # Verifica se o Player colidiu com um inimigo
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):

            ent1.health = 0  # Zera a vida do Player

            # Adiciona a explosão no ponto de colisão
            explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
            entity_list.append(explosion)

        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):

            ent2.health = 0  # Zera a vida do Player

            # Adiciona a explosão no ponto de colisão
            explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
            entity_list.append(explosion)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity], window):
        if enemy.health <= 0:


            players = [ent for ent in entity_list if isinstance(ent, Player)]  # Garante que só busca Players
            for player in players:
                player.score += enemy.score  # Atualiza o score do jogador



                if player.health <= 0:  # Mudando a condição para garantir que pega 0 ou menor


                    score = Score(window)
                    score.save(player.score)



    @staticmethod
    def verify_collision(entity_list: list[Entity], sprite_group):
        for ent1 in entity_list:
            if isinstance(ent1, Collision) or isinstance(ent1, Background):
                continue

            for ent2 in entity_list:
                if isinstance(ent2, Collision) or isinstance(ent2, Background):
                    continue

                if ent1 != ent2 and isinstance(ent1, Player) and isinstance(ent2, Enemy):
                    if ent1.rect.colliderect(ent2.rect):
                        print(f"Colisão detectada entre {ent1} e {ent2}")
                        explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
                        entity_list.append(explosion)
                        ent1.health = 0  # Zera a saúde do player após a colisão


    @staticmethod
    def verify_health(entity_list: list[Entity], window):
        for ent in entity_list:
            if hasattr(ent, 'health'):  # Verifica se a entidade tem 'health'
                if ent.health == 0:
                    if isinstance(ent, Enemy):
                        EntityMediator.__give_score(ent, entity_list, window)  # Atualiza o score do jogador
                    entity_list.remove(ent)  # Remove a entidade
                    print(f"Entidade {ent} removida da lista.")
                    if isinstance(ent, Player):  # Se o jogador morrer
                        print(f"Jogador {ent} morreu, indo para o menu!")

                        score = Score(window)
                        score.save(ent.score)

                        break  # Interrompe o loop
                        return

