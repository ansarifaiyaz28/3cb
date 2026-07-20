from pathlib import Path

import docker
from docker.errors import BuildError, DockerException, NotFound


def build_and_run() -> None:
    project_dir = Path("./odockerOnlyNmap").resolve()
    image_name = "my-app:latest"
    container_name = "my-app-container"

    try:
        # Connect using the same environment/config as the Docker CLI.
        client = docker.from_env()

        print(f"Building {image_name}...")

        image, build_logs = client.images.build(
            path=str(project_dir),
            tag=image_name,
            rm=True,
        )

        for entry in build_logs:
            if "stream" in entry:
                print(entry["stream"], end="")

        print("\nStarting container...")

        # remove any existing container with the same name
        try:
            old_container = client.containers.get(container_name)
            print(f"Removing existing container: {container_name}")
            old_container.remove(force=True)
        except NotFound:
            pass

        container = client.containers.run(
            image=image.id,
            detach=True,
            tty=True,          # Allocate a pseudo-TTY
            stdin_open=True,   # Keep stdin open
            ports={"5000/tcp": 5000},
            name=container_name,
        )

        print(f"Container started: {container.id}")
        print(container.logs(stream=False).decode())

    except BuildError as exc:
        print(f"Image build failed: {exc}")
    except DockerException as exc:
        print(f"Docker error: {exc}")


if __name__ == "__main__":
    build_and_run()