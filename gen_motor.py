#!/usr/bin/env python3
"""Generate 9 motor detail pages from produk.html shell."""
import re, urllib.parse

BASE = "/Users/naufal/Documents/Project/YMH Web/site"
shell = open(f"{BASE}/produk.html").read()

HEAD_LINKS = """<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0b0b0d">"""

MODELS = [
 dict(slug="nmax-turbo", name="NMAX Turbo", cat="MAXi Series", catkey="maxi",
  img="model-nmax-turbo.webp", imgalt="Yamaha NMAX Turbo",
  tag="Skutik premium 155cc dengan sensasi turbo elektrik.",
  desc=["Yamaha NMAX Turbo adalah varian tertinggi keluarga MAXi: mesin 155cc Blue Core VVA yang dipadukan transmisi elektrik YECVT. Lewat tombol Y-Shift, pengendara bisa memilih 3 level akselerasi instan — sensasi turbo yang bisa diatur sesuai kebutuhan, dari menyalip di jalan raya sampai stop-and-go di kota.",
   "Di luar performa, NMAX Turbo dibekali konektivitas Y-Connect, kontrol traksi (TCS), dan desain yang makin agresif. Unit tersedia di cabang Kopo, Soekarno-Hatta Bandung, dan Subang — lengkap dengan promo DP ringan dan potongan tenor bulan ini."],
  feats=[("YECVT + Y-Shift","Akselerasi elektrik 3 level yang bisa diatur pengendara."),
   ("155cc Blue Core VVA","Mesin efisien bertenaga dengan Variable Valve Actuation."),
   ("Y-Connect","Notifikasi pesan, info BBM, dan riwayat servis di aplikasi."),
   ("Desain Agresif","Tampilan MAXi premium dengan pencahayaan full LED.")],
  specs=[("Mesin","155cc, Blue Core, VVA"),("Transmisi","YECVT elektrik + Y-Shift"),("Fitur","Y-Connect, TCS, Smart Key"),("Pengereman","Cakram depan-belakang"),("Ideal untuk","Harian premium & touring")]),
 dict(slug="aerox-alpha", name="Aerox Alpha", cat="MAXi Series", catkey="maxi",
  img="model-aerox-alpha.webp", imgalt="Yamaha Aerox Alpha",
  tag="Sport scooter generasi terbaru untuk anak muda urban.",
  desc=["Aerox Alpha adalah generasi ketiga AEROX yang resmi meluncur Desember 2024: desain super sporty, fitur sarat teknologi canggih, dan mesin yang ditingkatkan. Karakter handling lincah khas MAXi dipertahankan, dengan ergonomi yang disempurnakan untuk harian maupun touring pendek.",
   "Buat kamu yang ingin tampil beda dan agresif setiap hari, Aerox Alpha adalah lifestyle item sekaligus kendaraan fungsional. Cek unitnya langsung di dealer atau minta simulasi kredit via WhatsApp."],
  feats=[("Desain Super Sporty","DNA R-Series dalam bodi skutik yang agresif."),
   ("155cc VVA","Performa responsif khas MAXi Yamaha."),
   ("Y-Connect","Terhubung ke aplikasi untuk info kendaraan."),
   ("Handling Lincah","Sasis rigid dan ringan untuk manuver kota.")],
  specs=[("Mesin","155cc, Blue Core, VVA"),("Transmisi","CVT otomatis"),("Fitur","Y-Connect, Smart Key"),("Pengereman","Cakram depan-belakang"),("Ideal untuk","Anak muda & komuter sporty")]),
 dict(slug="fazzio-hybrid", name="Fazzio Hybrid", cat="Classy Yamaha", catkey="classy",
  img="model-fazzio.webp", imgalt="Yamaha Fazzio Hybrid",
  tag="Skutik 125cc Hybrid retro-modern yang ikonik.",
  desc=["Yamaha Fazzio Hybrid memadukan mesin 125cc Blue Core Hybrid yang irit dengan desain retro-modern yang ikonik. Ringan, lincah, dan penuh gaya — favorit untuk mobilitas harian sekaligus tampil di konten.",
   "Teknologi hybrid membantu akselerasi awal sekaligus menjaga konsumsi BBM tetap hemat. Pengajuan kredit mudah: cukup KTP + KK, dibantu sampai ACC."],
  feats=[("Blue Core Hybrid 125","Irit dengan akselerasi awal responsif."),
   ("Desain Ikonik","Retro-modern yang timeless dan photogenic."),
   ("Ringan & Lincah","Mudah dikendarai semua kalangan."),
   ("Fitur Praktis","Double hook, answer back, dan bagasi lega.")],
  specs=[("Mesin","125cc, Blue Core Hybrid"),("Transmisi","CVT otomatis"),("Fitur","Smart Key, Answer Back"),("Pengereman","Cakram depan, tromol belakang"),("Ideal untuk","Harian stylish & pemula")]),
 dict(slug="grand-filano-hybrid", name="Grand Filano Hybrid", cat="Classy Yamaha", catkey="classy",
  img="model-grand-filano.webp", imgalt="Yamaha Grand Filano Hybrid",
  tag="Skutik fashion premium dengan teknologi hybrid.",
  desc=["Grand Filano Hybrid adalah skutik fashion premium Yamaha: tampilan elegan ala Eropa, teknologi hybrid yang efisien, dan jok luas yang nyaman untuk berboncengan. Cocok untuk mobilitas stylish sehari-hari.",
   "Dapatkan bonus aksesori dan perlindungan garansi resmi penuh untuk pembelian bulan ini di seluruh cabang Gerbang Cahaya."],
  feats=[("Hybrid 125","Efisiensi BBM dengan performa halus."),
   ("Premium Classic","Desain elegan yang berkelas."),
   ("Jok Luas","Nyaman untuk pengendara dan penumpang."),
   ("Full LED","Pencahayaan modern dan terang.")],
  specs=[("Mesin","125cc, Blue Core Hybrid"),("Transmisi","CVT otomatis"),("Fitur","Y-Connect, Smart Key"),("Pengereman","Cakram depan, tromol belakang"),("Ideal untuk","Fashion & komuter premium")]),
 dict(slug="gear-ultima", name="Gear Ultima 125 Hybrid", cat="Matic 125", catkey="matic",
  img="model-gear-ultima.webp", imgalt="Yamaha Gear Ultima 125 Hybrid",
  tag="Skutik multiguna untuk keluarga muda yang aktif.",
  desc=["Gear Ultima 125 Hybrid mengusung konsep skutik multiguna: mesin 125cc Blue Core Hybrid yang kuat namun irit, dek rata untuk barang, dan bagasi luas untuk aktivitas keluarga — dari antar anak sekolah sampai belanja mingguan.",
   "Diperkenalkan resmi di Bandung pada Maret 2025, Gear Ultima jadi jawaban mobilitas keluarga muda yang butuh satu motor untuk semua keperluan. Promo DP minim tersedia bulan ini."],
  feats=[("Multiguna","Dek rata + bagasi luas untuk keluarga."),
   ("Hybrid 125","Kuat membawa beban, tetap irit."),
   ("Tangguh Harian","Rangka kokoh untuk pemakaian intensif."),
   ("Praktis","Gantungan barang ganda dan socket charger.")],
  specs=[("Mesin","125cc, Blue Core Hybrid"),("Transmisi","CVT otomatis"),("Fitur","Double hook, answer back"),("Pengereman","Cakram depan, tromol belakang"),("Ideal untuk","Keluarga muda aktif")]),
 dict(slug="gear-125", name="Gear 125", cat="Matic 125", catkey="matic",
  img="model-gear-125.webp", imgalt="Yamaha Gear 125",
  tag="Matic tangguh, lincah, dan irit untuk harian.",
  desc=["Yamaha Gear 125 adalah pilihan rasional untuk mobilitas kota: ringan, irit, praktis, dengan fitur kekinian seperti double hook dan answer back system. Perawatan mudah dan biaya operasional rendah.",
   "Cocok untuk komuter, ojek online, maupun motor pertama. Tanya promo DP minim bulan ini ke admin kami."],
  feats=[("Irit & Bandel","Biaya operasional rendah untuk harian."),
   ("Lincah","Bodi kompak mudah selap-selip."),
   ("Fitur Kekinian","Double hook dan answer back."),
   ("Perawatan Mudah","Sparepart melimpah dan murah.")],
  specs=[("Mesin","125cc, Blue Core"),("Transmisi","CVT otomatis"),("Fitur","Answer back, double hook"),("Pengereman","Cakram depan, tromol belakang"),("Ideal untuk","Komuter & operasional")]),
 dict(slug="r25", name="YZF-R25", cat="Sport", catkey="sport",
  img="model-r25.webp", imgalt="Yamaha YZF-R25",
  tag="DNA R-Series 250cc dua silinder untuk pecinta kecepatan.",
  desc=["YZF-R25 membawa DNA balap R-Series: mesin 250cc dua silinder yang responsif, rangka diamond yang rigid, dan suspensi depan upside-down untuk handling presisi. Ergonomi balapnya tetap nyaman untuk jalan raya.",
   "Buat yang ingin naik kelas ke sport fairing sejati, R25 adalah gerbangnya. Konsultasikan skema kredit terbaik dengan admin kami."],
  feats=[("250cc 2 Silinder","Power halus khas sport Yamaha."),
   ("USD Fork","Handling presisi dan stabil."),
   ("R-DNA","Desain fairing aerodinamis ala MotoGP."),
   ("Rangka Diamond","Rigid untuk cornering percaya diri.")],
  specs=[("Mesin","250cc, 2 silinder"),("Transmisi","Manual 6 percepatan"),("Fitur","Assist & slipper clutch"),("Pengereman","Cakram depan-belakang"),("Ideal untuk","Sport & touring")]),
 dict(slug="wr155r", name="WR 155 R", cat="Off-Road", catkey="offroad",
  img="model-wr155r.webp", imgalt="Yamaha WR 155 R",
  tag="Motor trail 155cc siap segala medan.",
  desc=["Yamaha WR 155 R adalah motor trail berpendingin cairan dengan mesin 155cc VVA: suspensi teleskopik panjang, ground clearance tinggi, dan sasis ringan siap trabas maupun dipakai harian.",
   "Satu motor untuk dua dunia — jalur tanah akhir pekan dan jalanan kota Senin-Jumat. Tanya ketersediaan unit di cabang terdekat."],
  feats=[("155cc VVA Liquid-Cooled","Tenaga trail modern yang konsisten."),
   ("Suspensi Panjang","Meredam medan berat dengan nyaman."),
   ("Ground Clearance Tinggi","Siap jalur off-road."),
   ("Dual Purpose","Nyaman juga untuk harian.")],
  specs=[("Mesin","155cc, VVA, radiator"),("Transmisi","Manual 6 percepatan"),("Fitur","Speedometer digital"),("Pengereman","Cakram depan-belakang"),("Ideal untuk","Trabas & adventure")]),
 dict(slug="jupiter-z1", name="Jupiter Z1", cat="Moped", catkey="moped",
  img="model-jupiter-z1.webp", imgalt="Yamaha Jupiter Z1",
  tag="Bebek legendaris yang irit dan bandel.",
  desc=["Yamaha Jupiter Z1 adalah legenda motor bebek: mesin injeksi yang irit, sasis bandel untuk beban berat, dan perawatan yang mudah. Andalan untuk niaga maupun mobilitas harian.",
   "Suku cadang melimpah dan murah di seluruh bengkel kami. Pilihan paling ekonomis untuk operasional usaha."],
  feats=[("Injeksi Irit","Konsumsi BBM sangat efisien."),
   ("Bandel","Terbukti untuk niaga dan beban berat."),
   ("Murah Dirawat","Part melimpah dan terjangkau."),
   ("Praktis","Bagasi di bawah jok yang lega.")],
  specs=[("Mesin","±114cc, injeksi"),("Transmisi","Manual 4 percepatan"),("Fitur","Bagasi lega"),("Pengereman","Cakram depan, tromol belakang"),("Ideal untuk","Niaga & harian ekonomis")]),
]

def build(m):
    others = [x for x in MODELS if x["slug"] != m["slug"]]
    same = [x for x in others if x["catkey"] == m["catkey"]] + [x for x in others if x["catkey"] != m["catkey"]]
    rel = same[:3]
    wa = "https://wa.me/628997108328?text=" + urllib.parse.quote(f"Halo, saya tertarik dengan Yamaha {m['name']}. Minta info harga OTR & promo.")
    wa_tr = "https://wa.me/628997108328?text=" + urllib.parse.quote(f"Halo, saya ingin test ride Yamaha {m['name']}.")
    feats = "".join(f'<div class="step"><strong>{t}</strong><span>{d}</span></div>' for t, d in m["feats"])
    specs = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in m["specs"])
    relcards = "".join(
        f'<article class="model-card"><div class="ph"><img src="/assets/img/opt/{r["img"]}" alt="{r["imgalt"]}" loading="lazy"></div>'
        f'<div class="txt"><span class="cat">{r["cat"]}</span><h3>{r["name"]}</h3><p>{r["tag"]}</p>'
        f'<div class="row"><a class="btn btn-dark btn-sm" href="/motor/{r["slug"]}">Detail</a></div></div></article>' for r in rel)
    ld = ('{"@context":"https://schema.org","@type":"Product","name":"Yamaha %s","brand":{"@type":"Brand","name":"Yamaha"},'
          '"category":"%s","description":"%s","offers":{"@type":"Offer","availability":"https://schema.org/InStock",'
          '"seller":{"@type":"AutoDealer","name":"Yamaha Gerbang Cahaya"}}}' % (m["name"], m["cat"], m["tag"]))

    h = shell
    h = re.sub(r"<title>.*?</title>", f"<title>Yamaha {m['name']} — Harga OTR, Promo & Spesifikasi | Gerbang Cahaya</title>", h, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="Yamaha {m["name"]} di Gerbang Cahaya Bandung & Subang: {m["tag"]} Cek spesifikasi, promo kredit & booking test ride via WhatsApp.">', h, count=1)
    h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://yamahagerbangcahaya.id/motor/{m["slug"]}">', h, count=1)
    for prop, val in [
        ('og:title', f'Yamaha {m["name"]} | Gerbang Cahaya'),
        ('og:description', f'{m["tag"]} Promo & test ride tersedia.'),
        ('og:url', f'https://yamahagerbangcahaya.id/motor/{m["slug"]}'),
        ('og:image', f'https://yamahagerbangcahaya.id/assets/img/opt/{m["img"]}'),
        ('og:type', 'product')]:
        h = re.sub(f'<meta property="{prop}" content="[^"]*">', f'<meta property="{prop}" content="{val}">', h, count=1)
    h = re.sub(r'<script type="application/ld\+json">.*?</script>',
        f'<script type="application/ld+json">{ld}</script>', h, count=1, flags=re.S)
    main = f"""<main>
<section class="page-hero"><img src="/assets/img/opt/{m['img']}" alt="" aria-hidden="true" style="opacity:.25">
<div class="wrap"><p class="crumbs"><a href="/">Beranda</a> / <a href="/produk">Model</a> / {m['name']}</p>
<p class="eyebrow" style="color:#fff;opacity:.8">{m['cat']}</p>
<h1>Yamaha {m['name']}</h1>
<p>{m['tag']}</p></div>
</section>
<section class="section"><div class="wrap split">
<div class="media reveal"><img src="/assets/img/opt/{m['img']}" alt="{m['imgalt']} — dealer resmi Yamaha Bandung" style="background:radial-gradient(120% 100% at 50% 0%,#fff 40%,var(--wash) 100%)"></div>
<div class="reveal"><p class="eyebrow">{m['cat']}</p><h2>Kenapa {m['name']}?</h2>
<p>{m['desc'][0]}</p><p>{m['desc'][1]}</p>
<div style="display:flex;gap:12px;margin-top:26px;flex-wrap:wrap">
<a class="btn btn-primary" href="{wa}">Minta Penawaran</a>
<a class="btn btn-dark" href="/test-ride">Test Ride</a>
</div></div>
</div></section>
<section class="section wash"><div class="wrap">
<div class="sec-head reveal"><h2 class="sec-title">Spesifikasi</h2></div>
<div class="reveal" style="max-width:820px;margin:0 auto">
<table class="table-spec"><tbody>{specs}</tbody></table>
<p style="font-size:13.5px;color:var(--muted);margin-top:14px">Harga OTR mengikuti wilayah dan promo berjalan. <a href="{wa}">Chat admin</a> untuk angka pasti hari ini.</p>
</div></div></section>
<section class="section"><div class="wrap">
<div class="sec-head reveal"><h2 class="sec-title">Fitur Unggulan</h2></div>
<div class="steps reveal">{feats}</div>
<div style="text-align:center;margin-top:50px" class="reveal"><a class="btn btn-primary" href="{wa_tr}">Booking Test Ride {m['name']}</a></div>
</div></section>
<section class="section wash"><div class="wrap">
<div class="news-top reveal"><h2>Lihat Juga</h2><a class="link-more" href="/produk">Semua Model &rsaquo;</a></div>
<div class="model-grid reveal" style="grid-template-columns:repeat(3,1fr)">{relcards}</div>
</div></section>
</main>"""
    h = re.sub(r"<main>.*?</main>", lambda _: main, h, count=1, flags=re.S)
    return h

import os
os.makedirs(f"{BASE}/motor", exist_ok=True)
for m in MODELS:
    open(f"{BASE}/motor/{m['slug']}.html", "w").write(build(m))
    print("wrote", m["slug"])
