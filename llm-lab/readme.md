# Large Language Models' Lab

Some examples that explore the potential application fields of the LLM models.

## Environment

The programming environment consists of [Anaconda](https://www.anaconda.com/download) and an IDE; 
I use the paid version of [IntelliJ IDEA](https://www.jetbrains.com/idea/).

When using IntelliJ IDEA, it's necessary to declare the Anaconda's Python distribution as the interpreter for the project. 
Similarly, this must be done when using an alternative development environment.

![virtual](doc/conda_environment.png)

In order to use jupyter notebooks Intellij will prompt you for the permission to install the jupyter pacages in to the conda environment.

### Libraries

The following instructions add to the conda environment the libraries required for this lab

    > pip install -r requirements.txt 

### Huggingface Cache

    > huggingface-cli scan-cache


## Document's Summarization

- [Notebooks](./doc/jupyter_notebooks.md)
  - [PDF Summarization](./doc/jupyter_notebooks.md#example-n1)
  - [WEB Page Summarization](./doc/jupyter_notebooks.md#example-n2)
- [Applications](./doc/applications.md)
  - [Multiple Source Summarizer](./doc/applications.md#example-a1)

### References

#### Documentation

- [Hugging Face's Tranformers Docs](https://huggingface.co/docs/transformers/index)
- [Hugging Face's Tranformers GitHUB](https://github.com/huggingface/transformers)
- [haystack](https://github.com/deepdoctection/deepdoctection) by deepset

#### Libraries

- [DeepDoctection](https://github.com/deepdoctection/deepdoctection)
- [Detectron2](https://ai.meta.com/tools/detectron2/)
- [docTR](https://mindee.github.io/doctr/index.html)
- [fastText](https://fasttext.cc/docs/en/supervised-tutorial.html)
- [jdeskew](https://pypi.org/project/jdeskew/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [R-CNNs](https://d2l.ai/chapter_computer-vision/rcnn.html)
