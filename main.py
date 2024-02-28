from colorama import Fore 
import sys 
import time 
import os 
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
def loop_over(sequence,delay_time):
      for text in sequence:
            sys.stdout.flush()
            time.sleep(delay_time)
            sys.stdout.write(f'{text}')
      else:
            print(f'{colors[-1]}')
            
first_part_of_program_title=f'''
{colors[-2]}
                 ...............   ....
                 ................   .................        ...............          ....  ................    ...................     ...................
                 ...          ...    ...            ...    ...             ...        ....  ................   ...               ...    ...................
                 ...           ...   ...             ...   ...             ...        ....  ...                ...                              ....
                 ...          ...    ...             ...   ...             ...        ....  ...                ...                              ....
                 ...         ...     ...             ...   ...             ...        ....  ...                ...                              ....
                 ..............      ...                   ...             ...        ....  ................   ...                              .... 
                 ...                 ...                   ...             ...        ....  ................   ...                              ....
                 ...                 ...                   ...             ...   .... ....  ...                ...                              ....
                 ...                 ...                   ...             ...   .... ....  ...                ...                              ....
                 ...                 ...                   ...             ...   .........  ................   ...               ...            ....
                 ...                 ...                     ...............     .........  ................    ....................            .... 
                 '''
second_part_of_program_title=f'''
{colors[5]}
                  ..............     ....     ....  .....         ....            ...........             .................     ...............         ...............
                  ...          ...   ....     ....  ......        ....           ....      ....           .................   ...             ...       ...............
                  ...           ...  ....     ....  ........      ....          ....        ....          ....   ....  ....   ...              ...      ... 
                  ...           ...  ....     ....  .... ....     ....         ....          ....         ....   ....  ....   ...              ...      ...
                  ...           ...  .............  ....  ....    ....        .....           ....        ....   ....  ....   ...              ...      ...
                  ...           ...    .........    ....   ....   ....       ....              ....       ....   ....  ....   ...              ...      ............   
                  ...           ...       ....      ....    ....  ....      ........................      ....   ....  ....   ...              ...      ............
                  ...           ...       ....      ....     .... ....     ....                  ....     ....   ....  ....   ...              ...               ...
                  ...          ...        ....      ....      ........    ....                    ....    ....   ....  ....   ...              ...      ...      ...
                  ...         ...         ....      ....       .......   ....                      ....   ....   ....  ....   ...              ...      ............ 
                     ..........           ....      ....        ......  ....                        ....  ....   ....  ....      ...............        ............ '''
left_robot_arm_ascii_art=f'''
                  ____
                 /    \_\ 
                 |    | |
                 |   /_/
                /   | |
                |. .| |
                |   | |
                |. .| |
                |   | |
                (___)_)
                |___/_/
                  \_\_\_
                  /|||||
                  \|||||'''
robot_hands_ascii_art_prototype=f'''
                                 
                  {colors[2]}) {colors[1]}){colors[0]} ){colors[3]} )              {colors[2]}({colors[1]} ({colors[0]} ({colors[3]} (
                 {colors[2]}( {colors[1]}( {colors[0]}({colors[3]} (               {colors[2]} ){colors[1]} ){colors[0]} ){colors[3]} )
                 {colors[2]} ){colors[1]} ){colors[0]} ){colors[3]} )              {colors[2]}({colors[1]} ({colors[0]} ({colors[3]} (
                 {colors[2]}({colors[-1]}_{colors[1]}({colors[-1]}_{colors[0]}({colors[-1]}_{colors[3]}(___           {colors[-1]}__{colors[2]}){colors[-1]}_{colors[1]}){colors[-1]}_{colors[0]}){colors[-1]}_{colors[3]}){colors[-1]}_
                 /        \_\        /_/        \                             
                 |        |\○\      /{colors[3]}○{colors[-1]}/|        |
                 |________| \_\    /_/ |________|
                 |○||○|○|○|  \○\  /{colors[3]}○{colors[-1]}/  |{colors[3]}○{colors[-1]}||{colors[3]}○{colors[-1]}|{colors[3]}○{colors[-1]}|{colors[3]}○{colors[-1]}|
                 |_||_|_|_|   |_| |_|  |_||_|_|_|
                 \○\○\○\○\             /{colors[3]}○{colors[-1]}//{colors[3]}○{colors[-1]}/{colors[3]}○{colors[-1]}/{colors[3]}○{colors[-1]}/
                  \_\_\_\_\           /_//_/_/_/'''
ascii_art=f'''
{colors[-3]}
                  _____
                 /     /
                /     / |
               /_____/ / \        
               \/    \/ /   
                \_____\/\ 
               ___|  |__/___ 
         ____ /  /|  |  |/  /\__
        | __ /__/_______/\|/__  \                 
        \/__ \  /  {colors[-2]}---{colors[-3]} /   \   \/__ 
         /{colors[1]}_ {colors[-3]}/\  |  {colors[-2]}---{colors[-3]} |    \ / \ {colors[1]}_{colors[-3]}\ 
         {colors[1]}|_|{colors[-3]}  | |  {colors[-2]}---{colors[-3]} |    / |  {colors[1]}|_|{colors[-3]}
         \_ \_| |______|___/  |__/_/
        / /   \  (___(___)    /   \ \ 
       / /{colors[-2]}. .{colors[-3]} /  |   |   |    \ {colors[-2]}. .{colors[-3]}\ \ 
      / /    /   |   |   |     \    \ \       
     / / {colors[-2]}. .{colors[-3]}/    | {colors[3]}_ {colors[-3]}| {colors[3]}_ {colors[-3]}|      \{colors[-2]} . .{colors[-3]}\ \ 
    / /    /     | {colors[3]}_ {colors[-3]}| {colors[3]}_ {colors[-3]}|       \    \ \ 
    (_(___)      | {colors[3]}_ {colors[-3]}| {colors[3]}_ {colors[-3]}|        (___)_)
    \_\___| _____\___\___/____    |___/_/   
    /_/_/_//  /  /___/   \  \  \   \_\_\_    
    ||||| \|__|__\___\___/__|__|   /|||||
    ||||| //   / |       | \   \  \ /////   
           \__/__/       \__\__/     
           / / {colors[5]}__ {colors[-3]}\     / {colors[5]}__{colors[-3]} \ \ 
           | | {colors[5]}\/ {colors[-3]}/     \ {colors[5]}\/{colors[-3]} | |
           | |   |       |   | |
           |_|___/       \___|_| 
           (_(__)\       /(__)_)
           ||  {colors[1]}- -{colors[-3]}|      |{colors[1]}- -{colors[-3]}  ||
           ||  {colors[1]}- -{colors[-3]}\      /{colors[1]}- -{colors[-3]}  ||
           ||{colors[0]}_____/{colors[-3]}|    |\{colors[0]}_____{colors[-3]}||
           ||{colors[0]}____/ {colors[-3]}/    \ \{colors[0]}____{colors[-3]}||
           ||{colors[0]}___/{colors[-3]} /      \ \{colors[0]}___{colors[-3]}||
           ||{colors[0]}__/{colors[-3]} /        \ \{colors[0]}__{colors[-3]}||
           ||{colors[0]}_/ {colors[-3]}/          \ \{colors[0]}_{colors[-3]}||
           ||__/            \__||
           ((__/             \__))
          _|___|_           _|___|_
         /  {colors[2]}○  {colors[-3]}\__\        /__/ {colors[2]}○{colors[-3]}  \ 
        /______/__/        \__\_____\       '''
loop_over(sequence=f'{first_part_of_program_title}\n{second_part_of_program_title}',delay_time=0.001)
time.sleep(1)
os.system('cls')
time.sleep(1)
loop_over(sequence='Loading dynamos robot schematics...',delay_time=0.1)
print(robot_hands_ascii_art_prototype)