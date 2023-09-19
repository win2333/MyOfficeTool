import pikepdf
from pathlib import Path
import img2pdf
import shutil

origin_filename = "原始文件"


def convert_images_to_pdf(folder: Path):
    """转换文件夹中的图片到PDF"""
    for image_path in folder.glob('*'):
        if image_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            pdf_path = image_path.with_suffix('.pdf')
            with image_path.open("rb") as image_file:
                pdf_content = img2pdf.convert(image_file)
                pdf_path.write_bytes(pdf_content)


def move_files_to_original_folder(folder: Path, merged_pdf: Path):
    """
    将所有文件（除合并的PDF外）移至“原始文件”文件夹。
    Args:
    - folder (Path): 文件和PDF所在的文件夹。
    - merged_pdf (Path): 合并后的PDF的路径。
    """
    original_folder = folder / origin_filename
    original_folder.mkdir(exist_ok=True)

    for file_path in folder.iterdir():
        if file_path.name == merged_pdf.name or file_path.name == "原始文件" or file_path.is_dir():
            continue

        target_path = original_folder / file_path.name
        if target_path.exists():
            target_path.unlink()

        file_path.rename(target_path)


def merge_pdfs_with_pikepdf(folder: Path):
    """使用pikepdf合并文件夹中的所有PDF文件"""
    merged_pdf = folder / f"{folder.name}.pdf"
    if merged_pdf.exists():
        return
    pdf_files = sorted(folder.glob('*.pdf'))
    with pikepdf.open(pdf_files[0]) as pdf:
        for pdf_path in pdf_files[1:]:
            src = pikepdf.open(pdf_path)
            pdf.pages.extend(src.pages)
        pdf.save(merged_pdf)
    move_files_to_original_folder(folder, merged_pdf)


def main():
    script_folder = Path(__file__).parent
    for folder_path in script_folder.iterdir():
        if folder_path.is_dir():
            convert_images_to_pdf(folder_path)
            merge_pdfs_with_pikepdf(folder_path)


if __name__ == "__main__":
    main()
