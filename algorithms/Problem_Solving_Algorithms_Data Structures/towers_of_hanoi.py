def move_disk(from_pole, to_pole):
    print('moving disk from {} to {}'.format(from_pole, to_pole))


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        # move tower of size height-1 to helper:
        move_tower(height - 1, from_pole, with_pole, to_pole)

        # move disk from source pole to target pole
        move_disk(from_pole, to_pole)

        # move tower of size height-1 from helper to target
        move_tower(height - 1, with_pole, to_pole, from_pole)


move_tower(3, "A", "B", "C")
