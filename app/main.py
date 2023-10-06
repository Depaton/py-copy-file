def copy_file(command: str) -> None:
    action, file, new_file = command.split()
    if file != new_file:
        with (open(f"{file}", "r") as file_in,
              open(f"{new_file}", "w") as file_out):
            file_out.write(file_in.read())
