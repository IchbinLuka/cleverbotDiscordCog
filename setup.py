import setuptools

setuptools.setup(
    name="cleverbotcog",
    version="1.0",
    author="Luka Born",
    author_email="lukaborn@duck.com",
    url="https://github.com/IchbinLuka/cleverbotDiscordCog",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "nextcord~=2.0.0rc2",
        "cleverbotfreeapi~=1.1.1",
        "requests~=2.27.1"
    ],
    python_requires=">=3.10",
)
