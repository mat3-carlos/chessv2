import pygame

#Check time: Mantener las casillas que amenazan al rey (tapar el check) y las casillas a las que se puede mover el rey

pygame.init()
GAP = 120
TOP_GAP = 60
ALTO_CASILLA = 85
ANCHO_CASILLA = 85
ANCHO = ANCHO_CASILLA * 8 + GAP*2
ALTO = ALTO_CASILLA * 8 + GAP


layer_opacidad = pygame.Surface((ANCHO, ALTO))
layer_opacidad.set_colorkey((0, 0, 0))



pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Chess.com")
#icon
icon = pygame.image.load("assets/icon.webp")
icon = pygame.transform.scale(icon,(32,32))
pygame.display.set_icon(icon)
fuente = pygame.font.Font("freesansbold.ttf", 30)
fuente2 = pygame.font.Font("freesansbold.ttf", 40)
fuente_p = pygame.font.Font("freesansbold.ttf", 20)
fuente_p2 = pygame.font.Font("freesansbold.ttf", 15)

#SONIDOS-------------
move_sound = pygame.mixer.Sound("assets/move-self.mp3")
capture_sound = pygame.mixer.Sound("assets/capture.mp3")
check_sound = pygame.mixer.Sound("assets/move-check.mp3")
castle_sound = pygame.mixer.Sound("assets/castle.mp3")

#--------------


black_options = []
white_options = []


timer = pygame.time.Clock()
fps = 60
#game variables and images
piezas_blancas = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                   "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
location_negras = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
piezas_negras = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                   "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
location_blancas = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                 (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_blancas = []
captured_negras = []
#whites turn no selec = 0, whites turn selection = 1 | blacks turn no selec = 2,  blacks turn selection = 3
turn_step = 0
selection = 100

valid_moves = []
#load game piece images 
TMNO_GRD = 80
TMNO_PEQ = 45

#NEGRAS

black_queen = pygame.image.load("assets/bq.png")
black_queen = pygame.transform.scale(black_queen, (TMNO_GRD,TMNO_GRD))
black_queen_small = pygame.transform.scale(black_queen, (TMNO_PEQ,TMNO_PEQ))

black_rook = pygame.image.load("assets/br.png")
black_rook = pygame.transform.scale(black_rook, (TMNO_GRD,TMNO_GRD))
black_rook_small = pygame.transform.scale(black_rook, (TMNO_PEQ,TMNO_PEQ))

black_knight = pygame.image.load("assets/bn.png")
black_knight = pygame.transform.scale(black_knight, (TMNO_GRD,TMNO_GRD))
black_knight_small = pygame.transform.scale(black_knight, (TMNO_PEQ,TMNO_PEQ))

black_bishop = pygame.image.load("assets/bb.png")
black_bishop = pygame.transform.scale(black_bishop, (TMNO_GRD,TMNO_GRD))
black_bishop_small = pygame.transform.scale(black_bishop, (TMNO_PEQ,TMNO_PEQ))

black_king = pygame.image.load("assets/bk.png")
black_king = pygame.transform.scale(black_king, (TMNO_GRD,TMNO_GRD))
black_king_small = pygame.transform.scale(black_king, (TMNO_PEQ,TMNO_PEQ))

black_pawn = pygame.image.load("assets/bp.png")
black_pawn = pygame.transform.scale(black_pawn, (TMNO_GRD,TMNO_GRD))
black_pawn_small = pygame.transform.scale(black_pawn, (TMNO_PEQ,TMNO_PEQ))

#BLANCAS

white_queen = pygame.image.load("assets/wq.png")
white_queen = pygame.transform.scale(white_queen, (TMNO_GRD,TMNO_GRD))
white_queen_small = pygame.transform.scale(white_queen, (TMNO_PEQ,TMNO_PEQ))

white_rook = pygame.image.load("assets/wr.png")
white_rook = pygame.transform.scale(white_rook, (TMNO_GRD,TMNO_GRD))
white_rook_small = pygame.transform.scale(white_rook, (TMNO_PEQ,TMNO_PEQ))

white_knight = pygame.image.load("assets/wn.png")
white_knight = pygame.transform.scale(white_knight, (TMNO_GRD,TMNO_GRD))
white_knight_small = pygame.transform.scale(white_knight, (TMNO_PEQ,TMNO_PEQ))

white_bishop = pygame.image.load("assets/wb.png")
white_bishop = pygame.transform.scale(white_bishop, (TMNO_GRD,TMNO_GRD))
white_bishop_small = pygame.transform.scale(white_bishop, (TMNO_PEQ,TMNO_PEQ))

white_king = pygame.image.load("assets/wk.png")
white_king = pygame.transform.scale(white_king, (TMNO_GRD,TMNO_GRD))
white_king_small = pygame.transform.scale(white_king, (TMNO_PEQ,TMNO_PEQ))

white_pawn = pygame.image.load("assets/wp.png")
white_pawn = pygame.transform.scale(white_pawn, (TMNO_GRD,TMNO_GRD))
white_pawn_small = pygame.transform.scale(white_pawn, (TMNO_PEQ,TMNO_PEQ))

#listas

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]

small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]

#check variables / flashing counter
counter = 0

#drawing main board
def draw_board():
    pos_inicial_cuadrados = GAP/2
    ultimas_casillas = ALTO_CASILLA * 8 + GAP/2 - 20
    for i in range(8):
        letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for j in range(8):
            if (i + j) % 2 == 0:
                color_casilla = (235, 235, 208)
                color_numero = (235, 235, 208)
                color_letra = (119, 148, 85)
            else:
                color_casilla = (119, 148, 85)
                color_numero = (119, 148, 85)
                color_letra = (235, 235, 208)
            pygame.draw.rect(pantalla, color_casilla, ( i * ANCHO_CASILLA, pos_inicial_cuadrados+j * ALTO_CASILLA, ANCHO_CASILLA, ALTO_CASILLA))
            numero = fuente_p.render(str(8 - j), True, color_numero)
            letra = fuente_p.render(letras[i], True, color_letra)
            pantalla.blit(numero,(4,pos_inicial_cuadrados +4  + j * ALTO_CASILLA))
            pantalla.blit(letra,( 66 + i * ANCHO_CASILLA, ultimas_casillas))

    status_text = ["White's turn", "White's turn: piece selected", 
                   "Black's turn", "Black's turn: piece selected" ]
    pantalla.blit(fuente_p2.render(status_text[turn_step], True, (255, 255, 255)), (ANCHO -220, 20))

#draw pieces on board
def draw_pieces():



    for i in range(len(piezas_blancas)):
        index = piece_list.index(piezas_blancas[i])
        if turn_step < 2:
            if selection == i:
                rect_x = location_blancas[i][0] * ANCHO_CASILLA
                rect_y = location_blancas[i][1] * ALTO_CASILLA + GAP/2
                pygame.draw.rect(pantalla, (185, 203, 68), (rect_x, rect_y, ANCHO_CASILLA, ALTO_CASILLA))
                
        if piezas_blancas[i] == "pawn":
            pantalla.blit(white_pawn, (location_blancas[i][0] * ANCHO_CASILLA +2  , location_blancas[i][1] * ALTO_CASILLA + GAP/2))
        else:
            pantalla.blit(white_images[index], (location_blancas[i][0] * ANCHO_CASILLA +2  , location_blancas[i][1] * ALTO_CASILLA + GAP/2))

        

    for i in range(len(piezas_negras)):
        index = piece_list.index(piezas_negras[i])
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(pantalla, (185, 203, 68), (location_negras[i][0] * ANCHO_CASILLA , location_negras[i][1] * ALTO_CASILLA + GAP/2, ANCHO_CASILLA, ALTO_CASILLA))
        if piezas_negras[i] == "pawn":
            pantalla.blit(black_pawn, (location_negras[i][0] * ANCHO_CASILLA +2  , location_negras[i][1] * ALTO_CASILLA + GAP/2))
        else:
            pantalla.blit(black_images[index], (location_negras[i][0] * ANCHO_CASILLA +2  , location_negras[i][1] * ALTO_CASILLA + GAP/2))
        
#function to check all pieces valid options
def check_options(pieces, locations,turn): #Check all pieces valid options and return list of lists with valid moves for each piece
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == "pawn":
            moves_list = check_pawn(location, turn)
        if piece == "rook":
            moves_list = check_rook(location, turn)
        if piece == "knight":
            moves_list = check_knight(location, turn)
        if piece == "bishop":
            moves_list = check_bishop(location, turn)
        if piece == "queen":
            moves_list = check_queen(location, turn)
        if piece == "king":
            moves_list = check_king(location, turn)
        
        all_moves_list.append(moves_list)
        

    return all_moves_list



def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

def squares_between(a, b):
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay

    if dx == 0:
        step_x, step_y = 0, sign(dy)
    elif dy == 0:
        step_x, step_y = sign(dx), 0
    elif abs(dx) == abs(dy):
        step_x, step_y = sign(dx), sign(dy)
    else:
        return []

    out = []
    x, y = ax + step_x, ay + step_y
    while (x, y) != (bx, by):
        out.append((x, y))
        x += step_x
        y += step_y
    return out

def get_attackers_to_king(color):
    if color == "white":
        king_pos = location_blancas[piezas_blancas.index("king")]
        enemy_pieces = piezas_negras
        enemy_locs = location_negras
        enemy_options = check_options(enemy_pieces, enemy_locs, "black")
    else:
        king_pos = location_negras[piezas_negras.index("king")]
        enemy_pieces = piezas_blancas
        enemy_locs = location_blancas
        enemy_options = check_options(enemy_pieces, enemy_locs, "white")

    attackers = []
    for i, moves in enumerate(enemy_options):
        if king_pos in moves:
            attackers.append(i)
    return attackers

def get_check_response_squares(color, attacker_idx):
    if color == "white":
        king_pos = location_blancas[piezas_blancas.index("king")]
        enemy_piece = piezas_negras[attacker_idx]
        attacker_pos = location_negras[attacker_idx]
    else:
        king_pos = location_negras[piezas_negras.index("king")]
        enemy_piece = piezas_blancas[attacker_idx]
        attacker_pos = location_blancas[attacker_idx]

    response = {attacker_pos}  # capturar atacante siempre vale
    if enemy_piece in ("rook", "bishop", "queen"):
        for sq in squares_between(attacker_pos, king_pos):
            response.add(sq)  # bloquear rayo de ataque
    return response

def is_legal_move(color, piece_index, target):
    if color == "white":
        my_locs = location_blancas
        enemy_locs = location_negras
        enemy_pieces = piezas_negras
    else:
        my_locs = location_negras
        enemy_locs = location_blancas
        enemy_pieces = piezas_blancas

    original_pos = my_locs[piece_index]
    captured_piece = None
    captured_pos = None
    captured_idx = None

    my_locs[piece_index] = target
    if target in enemy_locs:
        captured_idx = enemy_locs.index(target)
        captured_pos = enemy_locs.pop(captured_idx)
        captured_piece = enemy_pieces.pop(captured_idx)

    in_check = jaque(color)

    my_locs[piece_index] = original_pos
    if captured_idx is not None:
        enemy_locs.insert(captured_idx, captured_pos)
        enemy_pieces.insert(captured_idx, captured_piece)

    return not in_check

def get_legal_options_for_color(color):
    if color == "white":
        my_pieces = piezas_blancas
        my_locs = location_blancas
        pseudo = check_options(my_pieces, my_locs, "white")
    else:
        my_pieces = piezas_negras
        my_locs = location_negras
        pseudo = check_options(my_pieces, my_locs, "black")

    attackers = get_attackers_to_king(color)

    filtered = []
    if len(attackers) == 0:
        filtered = [moves[:] for moves in pseudo]
    elif len(attackers) >= 2:
        for i, piece in enumerate(my_pieces):
            if piece == "king":
                filtered.append(pseudo[i][:])
            else:
                filtered.append([])
    else:
        response_squares = get_check_response_squares(color, attackers[0])
        for i, piece in enumerate(my_pieces):
            if piece == "king":
                filtered.append(pseudo[i][:])
            else:
                filtered.append([m for m in pseudo[i] if m in response_squares])

    legal = []
    for i, moves in enumerate(filtered):
        legal_moves = []
        for m in moves:
            if is_legal_move(color, i, m):
                legal_moves.append(m)
        legal.append(legal_moves)

    return legal

def update_all_options():
    global white_options, black_options
    white_options = get_legal_options_for_color("white")
    black_options = get_legal_options_for_color("black")
#CHECK PIECES:

def check_pawn(position,color):
    moves_list = []
    if color == "white":
        if (position[0], position[1] - 1) not in location_blancas and (position[0], position[1] - 1) not in location_negras and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in location_blancas and (position[0], position[1] - 2) not in location_negras and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0]-1,position[1] - 1 ) in location_negras:
            moves_list.append((position[0]-1,position[1] - 1 ))
        if (position[0]+1,position[1] - 1 ) in location_negras:
            moves_list.append((position[0]+1,position[1] - 1 ))



    else:
        if (position[0], position[1] + 1) not in location_negras and (position[0], position[1] + 1) not in location_blancas and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in location_negras and (position[0], position[1] + 2) not in location_blancas and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0]-1,position[1] + 1 ) in location_blancas:
            moves_list.append((position[0]-1,position[1] +1 ))
        if (position[0]+1,position[1] + 1 ) in location_blancas:
            moves_list.append((position[0]+1,position[1] +1 ))


    return moves_list

def check_rook(position,color):
    moves_list = []
    if color == "white":
        enemies_list = location_negras
        friends_list = location_blancas
    else: #Negras
        enemies_list = location_blancas
        friends_list = location_negras
    
    for i in range(4): # down, up, right, left
        path = True
        chain = 1
        if i == 0: #down
            x = 0
            y = 1
        elif i == 1: #up
            x = 0
            y = -1
        elif i == 2: #right
            x = 1
            y = 0
        else: #left
            x = -1
            y = 0
        while path:
            if (position[0] + x*chain, position[1] + y*chain) not in friends_list and \
            0 <= position[0] + x*chain < 8 and \
            0 <= position[1] + y*chain < 8:
                moves_list.append((position[0] + x*chain, position[1] + y*chain))
                if (position[0] + x*chain, position[1] + y*chain) in enemies_list:
                    path = False
                chain +=1
            else:
                path = False
                
               
        
    
     
    return moves_list

def check_knight(position,color):
    moves_list = []
    if color == "white":
        enemies_list = location_negras
        friends_list = location_blancas
    else: #Negras
        enemies_list = location_blancas
        friends_list = location_negras
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for move in knight_moves:
        new_position = (position[0] + move[0], position[1] + move[1])
        if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and \
        new_position not in friends_list:
                moves_list.append(new_position)


    return moves_list

def check_bishop(position,color):
    moves_list = []
    if color == "white":
        enemies_list = location_negras
        friends_list = location_blancas
    else: #Negras
        enemies_list = location_blancas
        friends_list = location_negras
    
    for i in range(4): # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0: #up-right
            x = 1
            y = -1
        elif i == 1: #up-left
            x = -1
            y = -1
        elif i == 2: #down-right
            x = 1
            y = 1
        else: #down-left
            x = -1
            y = 1
        while path:
            if (position[0] + x*chain, position[1] + y*chain) not in friends_list and \
            0 <= position[0] + x*chain < 8 and \
            0 <= position[1] + y*chain < 8:
                moves_list.append((position[0] + x*chain, position[1] + y*chain))
                if (position[0] + x*chain, position[1] + y*chain) in enemies_list:
                    path = False
                chain +=1
            else:
                path = False
        

    return moves_list

def check_queen(position,color):
    moves_list = []
    moves_list.extend(check_rook(position,color))
    moves_list.extend(check_bishop(position,color))

    return moves_list

def check_king(position,color):
    
    moves_list = []
    if color == "white":
        enemies_list = location_negras
        friends_list = location_blancas
        enemies_options = black_options

    else: #Negras
        enemies_list = location_blancas
        friends_list = location_negras
        enemies_options = white_options

    king_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for move in king_moves:
        new_position = (position[0] + move[0], position[1] + move[1])
        if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and \
        new_position not in friends_list:
            moves_list.append(new_position)

                        
    return moves_list



def jaque(color):
    return len(get_attackers_to_king(color)) > 0


        

#check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options

    valid_options = options_list[selection]
    return valid_options

#draw valid moves
def draw_valid(moves):
    color = (185, 203, 68)
    for i in range(len(moves)):
        if moves[i] in location_blancas or moves[i] in location_negras:
            pygame.draw.circle(layer_opacidad, "gray", (moves[i][0] * ANCHO_CASILLA + ANCHO_CASILLA//2, moves[i][1] * ALTO_CASILLA + GAP/2 + ALTO_CASILLA//2), ANCHO_CASILLA/2 , width=6)
            layer_opacidad.set_alpha(128)
            pantalla.blit(layer_opacidad, (0, 0))
        else:
            pygame.draw.circle(pantalla, color, (moves[i][0] * ANCHO_CASILLA + ANCHO_CASILLA//2, moves[i][1] * ALTO_CASILLA + GAP/2 + ALTO_CASILLA//2), 10)
    layer_opacidad.fill((0, 0, 0))

def draw_captured():
    for i in range(len(captured_blancas)):
        index = piece_list.index(captured_blancas[i])
        pantalla.blit(small_black_images[index], (10 + i * (TMNO_PEQ-10), ALTO - GAP/2 + 10))
    for i in range(len(captured_negras)):
        index = piece_list.index(captured_negras[i])
        pantalla.blit(small_white_images[index], (10 + i * (TMNO_PEQ-10), 10))

#draw check status
def draw_check():
    checked = False
    if turn_step < 2:
        king_index = piezas_blancas.index("king")
        if jaque("white"):
            if counter < 15:
                pygame.draw.rect(pantalla, (255, 107, 107), (location_blancas[king_index][0] * ANCHO_CASILLA, location_blancas[king_index][1] * ALTO_CASILLA + GAP/2, ANCHO_CASILLA, ALTO_CASILLA), width=5)
            checked = True
    else:
        king_index = piezas_negras.index("king")
        if jaque("black"):
            if counter < 15:
                pygame.draw.rect(pantalla, (255, 107, 107), (location_negras[king_index][0] * ANCHO_CASILLA, location_negras[king_index][1] * ALTO_CASILLA + GAP/2, ANCHO_CASILLA, ALTO_CASILLA), width=5)
            checked = True

#main game loop
update_all_options()
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter +=1
    else:
        counter = 0
    pantalla.fill((45, 43, 41))
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x = event.pos[0] // ANCHO_CASILLA
            mouse_y = (event.pos[1] - TOP_GAP) // ALTO_CASILLA

            # Ignore clicks outside the 8x8 board area.
            if not (0 <= mouse_x < 8 and 0 <= mouse_y < 8):
                continue

            click_coords = (mouse_x, mouse_y)

            #TURNO DE BLANCAS
            if turn_step <= 1: 
                
                if click_coords in location_blancas: 
                    selection = location_blancas.index(click_coords) #Selecciona pieza blanca
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    location_blancas[selection] = click_coords #Mover pieza blanca
                    if click_coords in location_negras:
                        black_piece = location_negras.index(click_coords) 
                        captured_blancas.append(piezas_negras[black_piece]) #Captura pieza negra
                        piezas_negras.pop(black_piece)
                        location_negras.pop(black_piece)
                        if jaque("black"):
                            check_sound.play()
                        else:
                            capture_sound.play()
                    elif jaque("black"):
                        check_sound.play()
                    else:
                        move_sound.play()

                    update_all_options() #Actualizar opciones después de mover pieza blanca
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                if turn_step == 1 and click_coords not in location_blancas: #Deseleccionar pieza blanca
                    selection = 100
                    turn_step = 0

            #TURNO DE NEGRAS
            if turn_step >= 2: 
                if click_coords in location_negras:
                    selection = location_negras.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    location_negras[selection] = click_coords
                    if click_coords in location_blancas:
                        white_piece = location_blancas.index(click_coords)
                        captured_negras.append(piezas_blancas[white_piece]) #Captura pieza blanca
                        piezas_blancas.pop(white_piece)
                        location_blancas.pop(white_piece)
                        if jaque("white"):
                            check_sound.play()
                        else:
                            capture_sound.play()
                    elif jaque("white"):
                        check_sound.play()
                    else:
                        move_sound.play()
                    
                    update_all_options() #Actualizar opciones después de mover pieza negra
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                if turn_step == 3 and click_coords not in location_negras:
                    selection = 100
                    turn_step = 2

    pygame.display.update()
pygame.quit()
