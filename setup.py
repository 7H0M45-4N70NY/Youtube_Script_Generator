from setuptools import find_packages,setup

setup(
    name='YouTube_Script_Generator',
    version='0.0.1',
    author='7H0M45-4NTONY',
    author_email='thomasantony14@gmail.com',
    install_requires=["llama-index-llms-gemini","youtube-transcript-api","streamlit","python-dotenv",],
    packages=find_packages()
)