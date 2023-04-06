from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import os

token = os.getenv("token")
os.mkdir("cards")

request = requests.get("https://sscompucare-api.onrender.com/files", headers={"Cookie": f"token={token}"})
files = request.json()

# import json
# files = json.loads(open("test-files.json", "r").read())

print(f"{len(files)} files found. Generating cards...")

for file in files:
    print("Generating card for '" + file["title"] + "...'")

    with open("file.png", "wb") as thumbnail_file:
        r = requests.get(file["thumbnailUrl"])  
        thumbnail_file.write(r.content)

    file_name = file["title"]
    file_logo = "file.png"

    base = Image.new("RGBA", (1200, 630), color=(238,238,238))

    for x in range(0,10):
        for y in range(0,10):
            logo_img = Image.open(file_logo).convert("RGBA")
            logo_img.thumbnail((210,210))
            base.paste(logo_img, (x*240, y*240), logo_img)

    background_overlay = Image.new("RGBA", base.size, color=(14, 165, 233, 240))
    base.paste(background_overlay, (0, 0), background_overlay)

    logo_img = Image.open("logo.png")
    base.paste(logo_img, (36, 532), logo_img)

    draw_company_name = ImageDraw.Draw(base)
    text = "S.S. Compucare"
    font = ImageFont.truetype('sans.ttf', 30)
    draw_company_name.text((138,551), text, font=font, fill='#F8FAFC', stroke_width=1, stroke_fill='#F8FAFC')

    draw_url = ImageDraw.Draw(base)
    text = "sscompucare.com"
    draw_url.text((901,551), text, font=font, fill='#F8FAFC', stroke_width=1, stroke_fill='#F8FAFC')

    draw_filename = ImageDraw.Draw(base)
    font = ImageFont.truetype('sans.ttf', 72)


    lines = textwrap.wrap(file_name, width=30)

    draw_filename.multiline_text((36,240), "\n".join(lines), font=font, fill='#F8FAFC', spacing=12, stroke_width=2, stroke_fill='#F8FAFC')

    base.save("cards/" + file["id"] + ".png")
    print("Completed.")

print(f"✅ {len(files)} cards generated succesfully.")