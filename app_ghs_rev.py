import streamlit as st

# ─────────────────────────────────────────────
# URL GAMBAR GHS (dari folder assets di GitHub)
# Ganti GITHUB_USER dan GITHUB_REPO sesuai repositori Anda
# ─────────────────────────────────────────────
GITHUB_USER = "dreamseeker76"
GITHUB_REPO = "GHS-B3-Identifier"
GITHUB_BRANCH = "main"        # ← nama branch

_BASE = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/assets"

GHS_IMG = {
    "GHS01": f"{_BASE}/explosive.png",
    "GHS02": f"{_BASE}/flammable.png",
    "GHS03": f"{_BASE}/oxidizing.png",
    "GHS04": f"{_BASE}/compressed_gas.png",
    "GHS05": f"{_BASE}/corrosive.png",
    "GHS06": f"{_BASE}/toxic.png",
    "GHS07": f"{_BASE}/harmful.png",
    "GHS08": f"{_BASE}/health_haz.png",
    "GHS09": f"{_BASE}/enviro_haz.png",
}

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="GHS B3 Identifier",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #0d0f14;
    color: #e8eaf0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111520 0%, #0d1826 100%);
    border-right: 1px solid #1e2a3a;
}
[data-testid="stSidebar"] * { color: #c8d4e0 !important; }
[data-testid="stSidebarNav"] { display: none; }

/* ── Cards ── */
.ghs-card {
    background: linear-gradient(135deg, #141c2e 0%, #0f1a2b 100%);
    border: 1px solid #1e3050;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    transition: border-color .25s, box-shadow .25s;
    cursor: pointer;
}
.ghs-card:hover {
    border-color: #f0a500;
    box-shadow: 0 0 20px rgba(240,165,0,.15);
}
.ghs-card-selected {
    border-color: #f0a500 !important;
    box-shadow: 0 0 28px rgba(240,165,0,.25) !important;
    background: linear-gradient(135deg, #1a2340 0%, #142035 100%) !important;
}

/* ── Symbol grid item ── */
.symbol-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.symbol-item {
    background: #141c2e;
    border: 2px solid #1e3050;
    border-radius: 12px;
    padding: 1rem .8rem;
    text-align: center;
    cursor: pointer;
    transition: all .2s;
}
.symbol-item:hover {
    border-color: #f0a500;
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(240,165,0,.18);
}
.symbol-emoji { font-size: 3rem; line-height: 1.2; display: block; }
.symbol-name {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 600;
    font-size: .9rem;
    color: #a0b4c8;
    margin-top: .4rem;
    display: block;
}

/* ── Detail box ── */
.detail-header {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #f0a500;
    letter-spacing: .04em;
}
.section-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: .75rem;
    font-weight: 600;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: #5a7a9a;
    margin-bottom: .4rem;
}
.tag {
    display: inline-block;
    background: rgba(240,165,0,.12);
    border: 1px solid rgba(240,165,0,.3);
    color: #f0c060;
    border-radius: 6px;
    padding: .25rem .7rem;
    font-size: .82rem;
    font-family: 'IBM Plex Mono';
    margin: .2rem .2rem .2rem 0;
}
.emergency-box {
    background: rgba(220,50,50,.08);
    border-left: 4px solid #dc3232;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.2rem;
    margin-top: .5rem;
}
.apd-box {
    background: rgba(30,140,200,.08);
    border-left: 4px solid #1e8cc8;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.2rem;
    margin-top: .5rem;
}
.welcome-hero {
    background: linear-gradient(135deg, #0f1e35 0%, #141c2e 60%, #0d1218 100%);
    border: 1px solid #1e3050;
    border-radius: 18px;
    padding: 3rem 2.5rem;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.welcome-hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(240,165,0,.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #f0a500;
    letter-spacing: .06em;
    margin-bottom: .4rem;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #7a9ab8;
    max-width: 600px;
    margin: 0 auto 1.5rem;
    line-height: 1.65;
}
.info-pill {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    background: rgba(240,165,0,.1);
    border: 1px solid rgba(240,165,0,.2);
    border-radius: 30px;
    padding: .35rem 1rem;
    font-size: .85rem;
    color: #d4a840;
    margin: .25rem;
}
.about-card {
    background: #141c2e;
    border: 1px solid #1e3050;
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.team-card {
    background: linear-gradient(135deg, #141c2e, #0f1826);
    border: 1px solid #1e3050;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}
.team-avatar {
    width: 60px; height: 60px;
    background: linear-gradient(135deg, #f0a500, #c47800);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    margin: 0 auto .8rem;
}
.divider {
    border: none;
    border-top: 1px solid #1e2a3a;
    margin: 1.5rem 0;
}
h2 { font-family: 'Rajdhani', sans-serif; font-weight: 700; color: #d0dce8; letter-spacing:.03em; }
h3 { font-family: 'Rajdhani', sans-serif; font-weight: 600; color: #a0b8cc; }
p  { color: #8090a8; line-height: 1.7; }
li { color: #8090a8; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA GHS
# ─────────────────────────────────────────────
GHS_DATA = {
    "GHS01 – Bahan Peledak": {
        "emoji": "💥",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/GHS-pictogram-explos.svg/240px-GHS-pictogram-explos.svg.png",
        "code": "GHS01",
        "kategori": "Explosives",
        "bahaya": [
            "Bahan/campuran yang dapat meledak secara massal",
            "Bahan yang sangat tidak stabil, sensitif terhadap benturan, gesekan, api, atau panas",
            "Peroksida organik dengan sensitivitas tinggi",
        ],
        "contoh": ["TNT", "Nitrat amonium", "Kembang api", "Peroksida organik tipe A/B"],
        "apd": [
            "🥽 Pelindung wajah penuh (face shield)",
            "🧤 Sarung tangan anti-ledakan",
            "👘 Pakaian pelindung tahan api",
            "👂 Pelindung telinga",
            "🦺 Rompi anti-fragmentasi (jika diperlukan)",
        ],
        "penyimpanan": "Simpan di gudang terpisah, jauh dari sumber panas, api, dan bahan oksidator. Batasi jumlah penyimpanan.",
        "darurat": [
            "🚨 Evakuasi segera semua personel dari area ledakan minimal 300 meter",
            "📞 Hubungi tim penjinak bahan berbahaya (Tim Damkar/HAZMAT)",
            "🚒 Laporkan ke 113 (Pemadam Kebakaran) dan 119 (Ambulans)",
            "🚫 JANGAN coba memadamkan api jika melibatkan bahan peledak",
            "🧯 Isolasi area dan tunggu petugas berwenang",
            "📋 Catat jenis bahan dan kuantitas untuk dilaporkan ke petugas",
        ],
    },
    "GHS02 – Bahan Mudah Terbakar": {
        "emoji": "🔥",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/GHS-pictogram-flamme.svg/240px-GHS-pictogram-flamme.svg.png",
        "code": "GHS02",
        "kategori": "Flammables",
        "bahaya": [
            "Gas, aerosol, cairan, dan padatan yang mudah terbakar",
            "Bahan piroforik (menyala sendiri di udara)",
            "Bahan yang reaktif terhadap air menghasilkan gas mudah terbakar",
        ],
        "contoh": ["Aseton", "Etanol", "Bensin", "Hidrogen", "Natrium logam"],
        "apd": [
            "🥽 Kacamata pengaman / pelindung wajah",
            "🧤 Sarung tangan tahan bahan kimia",
            "👘 Pakaian pelindung tahan api / overall anti-statis",
            "👟 Sepatu anti-statis",
            "🌬️ Respirator jika uap berbahaya",
        ],
        "penyimpanan": "Simpan di tempat sejuk, berventilasi baik, jauh dari sumber nyala api dan percikan. Gunakan lemari penyimpanan khusus flammable.",
        "darurat": [
            "🚒 Hubungi pemadam kebakaran: 113",
            "🔥 Padamkan api kecil dengan APAR jenis CO₂ atau dry powder",
            "💧 JANGAN gunakan air untuk cairan mudah terbakar (menyebabkan api menyebar)",
            "💨 Ventilasikan area untuk mencegah akumulasi uap",
            "⚡ Matikan semua sumber listrik dan nyala api di sekitar area",
            "🚫 Jauhkan dari area terbuka yang berpotensi membentuk awan uap",
        ],
    },
    "GHS03 – Bahan Pengoksidasi": {
        "emoji": "🔶",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/GHS-pictogram-rondflam.svg/240px-GHS-pictogram-rondflam.svg.png",
        "code": "GHS03",
        "kategori": "Oxidizers",
        "bahaya": [
            "Dapat menyebabkan atau memperparah kebakaran",
            "Dapat menyebabkan ledakan jika kontak dengan bahan mudah terbakar",
            "Melepaskan oksigen yang meningkatkan intensitas pembakaran",
        ],
        "contoh": ["Hidrogen peroksida", "Kalium permanganat", "Asam nitrat pekat", "Klorin"],
        "apd": [
            "🥽 Kacamata pengaman kimia (splash goggles)",
            "🧤 Sarung tangan karet/neoprene",
            "👘 Apron kimia atau pakaian pelindung",
            "🌬️ Respirator dengan filter oksidan jika diperlukan",
        ],
        "penyimpanan": "Pisahkan dari bahan mudah terbakar dan bahan organik. Simpan di tempat dingin dan kering. Hindari kontaminasi.",
        "darurat": [
            "🚿 Siram segera dengan air banyak jika kontak kulit/mata minimal 15 menit",
            "🏥 Segera cari bantuan medis: 119",
            "💨 Ventilasikan area – gas oksidan dapat menyebabkan sesak napas",
            "🚫 Jauhkan dari bahan mudah terbakar untuk mencegah kebakaran hebat",
            "🧯 Gunakan air dalam jumlah besar untuk memadamkan kebakaran yang melibatkan oksidator",
            "📞 Hubungi BPBD atau tim HAZMAT setempat",
        ],
    },
    "GHS04 – Gas Bertekanan": {
        "emoji": "🫙",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/GHS-pictogram-bottle.svg/240px-GHS-pictogram-bottle.svg.png",
        "code": "GHS04",
        "kategori": "Compressed Gases",
        "bahaya": [
            "Silinder dapat meledak jika dipanaskan",
            "Gas kriogenik dapat menyebabkan luka bakar dingin",
            "Risiko kekurangan oksigen di ruang tertutup (gas inert)",
        ],
        "contoh": ["Oksigen", "Nitrogen", "LPG", "Helium", "Gas Asetilen"],
        "apd": [
            "🥽 Pelindung wajah penuh untuk gas kriogenik",
            "🧤 Sarung tangan kriogenik (untuk LN₂, LO₂)",
            "👘 Pakaian isolasi untuk gas dingin",
            "👟 Sepatu safety berat",
            "🌬️ SCBA (Self-Contained Breathing Apparatus) jika di ruang tertutup",
        ],
        "penyimpanan": "Simpan silinder tegak lurus, ikat dengan rantai pengaman. Jauhkan dari panas. Simpan gas yang bisa terbakar terpisah dari gas pengoksidasi.",
        "darurat": [
            "💨 Evakuasi jika terjadi kebocoran gas di ruang tertutup",
            "🌬️ Ventilasikan area segera",
            "🚫 Jangan coba menutup katup jika ada api (bahaya meledak)",
            "🧊 Siram silinder yang panas dengan air (jangan biarkan kering)",
            "📞 Hubungi pemasok gas atau tim HAZMAT: 119 / 112",
            "🏥 Beri oksigen pada korban yang menghirup gas inert",
        ],
    },
    "GHS05 – Bahan Korosif": {
        "emoji": "🧪",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/GHS-pictogram-acid.svg/240px-GHS-pictogram-acid.svg.png",
        "code": "GHS05",
        "kategori": "Corrosives",
        "bahaya": [
            "Dapat merusak jaringan kulit, mata, dan saluran pernapasan",
            "Menyebabkan korosi pada logam",
            "Asam kuat dan basa kuat termasuk kategori ini",
        ],
        "contoh": ["Asam sulfat", "Asam klorida", "NaOH", "KOH", "Asam asetat glasial"],
        "apd": [
            "🥽 Kacamata splash-proof atau pelindung wajah penuh",
            "🧤 Sarung tangan karet tebal / PVC",
            "👘 Apron kimia tahan asam/basa",
            "👟 Sepatu bot karet",
            "🌬️ Respirator dengan filter asam/basa jika uap signifikan",
        ],
        "penyimpanan": "Simpan dalam wadah tahan korosi. Pisahkan asam dari basa. Simpan di lemari dengan ventilasi dan baki penampung tumpahan.",
        "darurat": [
            "🚿 Cuci segera dengan air mengalir minimal 15–20 menit (kulit/mata)",
            "👁️ Untuk mata: bilas terus dan segera ke dokter",
            "🚫 JANGAN netralisasi bahan kimia yang mengenai kulit (dapat memperparah)",
            "🏥 Segera ke fasilitas kesehatan: 119",
            "💨 Hindari menghirup uap – gunakan respirator atau jauhi area",
            "🧯 Tumpahan: tutupi dengan pasir kering atau material inert, jangan gunakan air langsung",
        ],
    },
    "GHS06 – Toksik Akut": {
        "emoji": "☠️",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/GHS-pictogram-skull.svg/240px-GHS-pictogram-skull.svg.png",
        "code": "GHS06",
        "kategori": "Acute Toxicity",
        "bahaya": [
            "Berbahaya atau fatal jika tertelan, terhirup, atau terserap kulit",
            "Toksisitas tinggi meskipun dalam dosis kecil",
            "Kategori 1–3 (sangat toksik hingga toksik)",
        ],
        "contoh": ["Sianida", "Merkuri", "Arsenik", "Pestisida karbamat", "Metanol"],
        "apd": [
            "🌬️ SCBA atau respirator full-face dengan filter kimia",
            "🧤 Sarung tangan kimia ganda (double glove)",
            "👘 Pakaian pelindung Level B atau C",
            "👟 Sepatu bot kimia",
            "🥽 Pelindung wajah penuh",
        ],
        "penyimpanan": "Simpan dalam lemari terkunci. Catat setiap pengambilan. Jauhkan dari jangkauan orang yang tidak berwenang.",
        "darurat": [
            "📞 Hubungi Poison Control / RS Terdekat: 119 atau 021-4250767 (RSCM Jakarta)",
            "🚫 JANGAN paksakan muntah kecuali atas instruksi dokter",
            "🌬️ Pindahkan korban ke udara segar segera",
            "🏥 Bawa ke UGD rumah sakit dengan membawa lembar MSDS/SDS bahan",
            "🧤 Gunakan APD saat menangani korban terkontaminasi",
            "💧 Cuci area kulit yang terkontaminasi dengan air dan sabun minimal 15 menit",
        ],
    },
    "GHS07 – Berbahaya": {
        "emoji": "⚠️",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/GHS-pictogram-exclam.svg/240px-GHS-pictogram-exclam.svg.png",
        "code": "GHS07",
        "kategori": "Harmful / Irritant",
        "bahaya": [
            "Iritan kulit dan mata",
            "Sensitisasi kulit",
            "Toksik akut kategori 4 (bahaya lebih rendah)",
            "Narkotik/sedatif ringan jika terhirup",
        ],
        "contoh": ["Aseton", "Toluena", "Xilena", "Etil asetat", "Isopropanol"],
        "apd": [
            "🥽 Kacamata pengaman",
            "🧤 Sarung tangan nitrile",
            "👘 Jas lab / overall",
            "🌬️ Masker respirator jika ventilasi kurang",
        ],
        "penyimpanan": "Simpan di tempat berventilasi baik. Wadah harus tertutup rapat. Jauhkan dari panas berlebih.",
        "darurat": [
            "🚿 Cuci kulit dengan sabun dan air jika terpapar",
            "👁️ Bilas mata dengan air bersih minimal 10 menit",
            "🌬️ Bawa ke udara segar jika terhirup",
            "🏥 Konsultasikan ke dokter jika gejala berlanjut",
            "📋 Laporkan paparan ke K3 perusahaan",
        ],
    },
    "GHS08 – Bahaya Kesehatan Jangka Panjang": {
        "emoji": "🫁",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/GHS-pictogram-silhouette.svg/240px-GHS-pictogram-silhouette.svg.png",
        "code": "GHS08",
        "kategori": "Health Hazard",
        "bahaya": [
            "Karsinogen (penyebab kanker)",
            "Mutagen (merusak materi genetik)",
            "Toksik reproduksi",
            "Sensitisasi saluran napas",
            "Toksisitas organ target spesifik",
        ],
        "contoh": ["Benzena", "Formaldehida", "Asbestos", "Timbal", "Silika kristalin"],
        "apd": [
            "🌬️ Respirator N95/P100 atau supplied-air respirator",
            "🧤 Sarung tangan kimia sesuai bahan",
            "👘 Pakaian pelindung lengkap (coverall)",
            "🥽 Kacamata atau pelindung wajah",
            "👟 Sepatu safety tertutup",
        ],
        "penyimpanan": "Simpan sesuai SDS. Pantau paparan dengan alat ukur. Lakukan pemantauan kesehatan berkala bagi pekerja yang terpapar.",
        "darurat": [
            "🏥 Paparan kronis: konsultasi ke dokter spesialis K3/okupasi",
            "🌬️ Paparan akut: bawa ke udara segar, beri oksigen jika perlu",
            "📋 Dokumentasikan setiap paparan dalam rekam medis pekerja",
            "🚿 Segera bersihkan kontaminasi dari kulit/pakaian",
            "📞 Lapor ke dokter perusahaan / Dinkes setempat",
            "🔍 Lakukan pemeriksaan medis rutin (medical surveillance)",
        ],
    },
    "GHS09 – Bahaya Lingkungan": {
        "emoji": "🌿",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/GHS-pictogram-aquatic-pollutant.svg/240px-GHS-pictogram-aquatic-pollutant.svg.png",
        "code": "GHS09",
        "kategori": "Environmental Hazard",
        "bahaya": [
            "Toksik terhadap organisme akuatik",
            "Efek jangka panjang pada ekosistem perairan",
            "Bioakumulasi dalam rantai makanan",
        ],
        "contoh": ["Tributiltin", "DDT", "PCB", "Surfaktan nonionik", "Beberapa logam berat"],
        "apd": [
            "🥽 Kacamata pengaman",
            "🧤 Sarung tangan kimia",
            "👘 Pakaian pelindung",
            "👟 Sepatu bot (jika potensi tumpahan)",
        ],
        "penyimpanan": "Simpan jauh dari saluran air/drainase. Gunakan baki penampung (spill tray). Pastikan penyimpanan kedap.",
        "darurat": [
            "🚫 Cegah masuknya bahan ke saluran air, got, atau sungai",
            "🧱 Bendung tumpahan dengan pasir atau material absorben",
            "📞 Laporkan tumpahan ke KLHK / Dinas Lingkungan Hidup setempat",
            "📋 Dokumentasikan insiden untuk pelaporan lingkungan",
            "🧹 Kumpulkan material terkontaminasi sebagai limbah B3",
            "🌊 Jika mencapai badan air, segera notifikasi pihak berwenang",
        ],
    },
}

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:.8rem 0 1.4rem;'>
        <div style='font-family:Rajdhani,sans-serif;font-size:1.5rem;font-weight:700;
                    color:#f0a500;letter-spacing:.06em;'>⚗️ GHS B3</div>
        <div style='font-size:.75rem;color:#4a6a8a;letter-spacing:.1em;
                    text-transform:uppercase;margin-top:.1rem;'>Identifier System</div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Navigasi",
        ["🏠  Beranda", "🔬  Identifikasi Simbol", "ℹ️  Tentang Aplikasi"],
        label_visibility="collapsed",
    )

    st.markdown("<hr style='border-color:#1e2a3a;margin:1.2rem 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:.72rem;color:#3a5a7a;line-height:1.6;'>
        <b style='color:#4a7a9a;'>Released on June 7th, 2026<br>
        Versi:</b> 1.0.0<br>
        <b style='color:#4a7a9a;'>Basis Regulasi:</b><br>
        PP No. 22/2021 · PermenLHK P.12/2020<br>
        GHS Rev. 10 (2023) · ISO 11014
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HALAMAN 1 – BERANDA
# ─────────────────────────────────────────────
if menu == "🏠  Beranda":
    st.markdown("""
    <div class='welcome-hero'>
        <div style='font-size:3.5rem;margin-bottom:.5rem;'>⚗️</div>
        <div class='hero-title'>Selamat Datang di GHS B3 Identifier</div>
        <div class='hero-subtitle'>
            Sistem identifikasi simbol bahaya bahan kimia berbasis 
            <b style='color:#d4a840;'>Globally Harmonized System (GHS)</b> — 
            dirancang untuk mendukung keselamatan kerja dan pengelolaan B3 
            yang tepat di lingkungan industri maupun laboratorium.
        </div>
        <div>
            <span class='info-pill'>✅ 9 Simbol GHS Lengkap</span>
            <span class='info-pill'>🛡️ Panduan APD</span>
            <span class='info-pill'>🚨 Tindakan Darurat</span>
            <span class='info-pill'>📋 Sesuai Regulasi Indonesia</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='ghs-card'>
            <div style='font-size:2rem;'>🔬</div>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.15rem;font-weight:700;
                        color:#d0dce8;margin:.6rem 0 .3rem;'>Identifikasi Cepat</div>
            <p style='font-size:.85rem;margin:0;'>Pilih simbol GHS dan dapatkan informasi lengkap bahaya, APD yang wajib digunakan, serta langkah penanganan darurat.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='ghs-card'>
            <div style='font-size:2rem;'>🛡️</div>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.15rem;font-weight:700;
                        color:#d0dce8;margin:.6rem 0 .3rem;'>Panduan APD</div>
            <p style='font-size:.85rem;margin:0;'>Rekomendasi Alat Pelindung Diri (APD) yang sesuai untuk setiap kategori bahaya bahan kimia berbasis GHS.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='ghs-card'>
            <div style='font-size:2rem;'>🚨</div>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.15rem;font-weight:700;
                        color:#d0dce8;margin:.6rem 0 .3rem;'>Prosedur Darurat</div>
            <p style='font-size:.85rem;margin:0;'>Langkah-langkah tindakan darurat yang harus dilakukan saat terjadi insiden atau kecelakaan kerja dengan B3.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🗺️ Panduan Penggunaan Aplikasi")

    steps = [
        ("1", "Buka Menu Identifikasi", "Pilih menu **🔬 Identifikasi Simbol** di sidebar kiri."),
        ("2", "Pilih Simbol GHS", "Klik salah satu dari 9 simbol GHS yang tersedia pada grid simbol."),
        ("3", "Baca Informasi Bahaya", "Pelajari deskripsi bahaya, contoh bahan kimia, dan kategori risiko."),
        ("4", "Siapkan APD", "Ikuti rekomendasi Alat Pelindung Diri yang sesuai sebelum bekerja."),
        ("5", "Tindakan Darurat", "Hafal prosedur darurat untuk penanganan insiden yang cepat dan tepat."),
    ]
    for num, title, desc in steps:
        st.markdown(f"""
        <div class='ghs-card' style='display:flex;align-items:flex-start;gap:1rem;'>
            <div style='min-width:36px;height:36px;background:rgba(240,165,0,.15);
                        border:2px solid #f0a500;border-radius:50%;display:flex;
                        align-items:center;justify-content:center;
                        font-family:Rajdhani,sans-serif;font-weight:700;
                        font-size:1rem;color:#f0a500;'>{num}</div>
            <div>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;
                            font-size:1rem;color:#d0dce8;margin-bottom:.2rem;'>{title}</div>
                <p style='font-size:.87rem;margin:0;'>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:rgba(220,50,50,.07);border:1px solid rgba(220,50,50,.2);
                border-radius:12px;padding:1.2rem 1.5rem;'>
        <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:1rem;
                    color:#e05050;margin-bottom:.4rem;'>⚠️ Disclaimer</div>
        <p style='font-size:.84rem;margin:0;'>
            Informasi dalam aplikasi ini bersifat umum dan edukatif. Untuk prosedur keselamatan resmi, 
            selalu rujuk pada <b style='color:#a0b8cc;'>Safety Data Sheet (SDS/MSDS)</b> dari produsen bahan kimia 
            dan prosedur K3 yang berlaku di institusi Anda.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HALAMAN 2 – IDENTIFIKASI SIMBOL
# ─────────────────────────────────────────────
elif menu == "🔬  Identifikasi Simbol":
    st.markdown("## 🔬 Identifikasi Simbol Bahaya GHS")
    st.markdown("<p style='margin-top:-.5rem;'>Pilih simbol GHS di bawah ini untuk melihat informasi lengkap.</p>", unsafe_allow_html=True)

    if "selected_ghs" not in st.session_state:
        st.session_state.selected_ghs = None

    # Grid simbol
    keys = list(GHS_DATA.keys())
    cols = st.columns(5)
    for i, key in enumerate(keys):
        d = GHS_DATA[key]
        is_sel = st.session_state.selected_ghs == key
        border_color = "#f0a500" if is_sel else "#1e3050"
        bg_color = "#1a2340" if is_sel else "#141c2e"
        label_color = "#f0a500" if is_sel else "#5a7a9a"
        img_url = GHS_IMG[d["code"]]
        with cols[i % 5]:
            st.markdown(f"""
            <div style='background:{bg_color};border:2px solid {border_color};
                    border-radius:12px;padding:.8rem;text-align:center;
                    margin-bottom:.3rem;'>
                <img src="{img_url}" style="width:72px;height:72px;object-fit:contain;" />
                <div style='font-family:Rajdhani,sans-serif;font-size:.8rem;font-weight:600;
                        color:{label_color};margin-top:.3rem;'>{d['code']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Pilih", key=f"btn_{i}", use_container_width=True):
                st.session_state.selected_ghs = key
                st.rerun()
    st.markdown("<hr style='border-color:#1e2a3a;margin:1.5rem 0;'>", unsafe_allow_html=True)

    if st.session_state.selected_ghs:
        key = st.session_state.selected_ghs
        d = GHS_DATA[key]

        col_left, col_right = st.columns([1, 2])

        with col_left:
            img_url_detail = GHS_IMG[d["code"]]
            st.markdown(f"""
            <div style='background:linear-gradient(135deg,#141c2e,#0f1826);
                        border:2px solid #f0a500;border-radius:16px;
                        padding:2rem;text-align:center;'>
                <img src="{img_url_detail}" style="width:130px;height:130px;object-fit:contain;" />
                <div style='font-family:Rajdhani,sans-serif;font-size:1.4rem;
                            font-weight:700;color:#f0a500;margin:.8rem 0 .2rem;'>{d['code']}</div>
                <div style='font-size:.8rem;color:#5a8aaa;letter-spacing:.1em;
                            text-transform:uppercase;'>{d['kategori']}</div>
            </div>
            <br>
            <div class='about-card'>
                <div class='section-label'>Contoh Bahan Kimia</div>
            """, unsafe_allow_html=True)
            for c in d["contoh"]:
                st.markdown(f"<span class='tag'>{c}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class='about-card'>
                <div class='section-label'>Cara Penyimpanan</div>
                <p style='font-size:.85rem;margin:0;'>{d['penyimpanan']}</p>
            </div>
            """, unsafe_allow_html=True)

        with col_right:
            st.markdown(f"<div class='detail-header'>{key}</div>", unsafe_allow_html=True)

            st.markdown("<div class='section-label' style='margin-top:1rem;'>Deskripsi Bahaya</div>", unsafe_allow_html=True)
            for b in d["bahaya"]:
                st.markdown(f"""
                <div style='display:flex;align-items:flex-start;gap:.6rem;margin-bottom:.4rem;'>
                    <span style='color:#f0a500;margin-top:.1rem;'>▸</span>
                    <span style='font-size:.9rem;color:#a0b8cc;'>{b}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<div class='section-label' style='margin-top:1.2rem;'>Alat Pelindung Diri (APD)</div>", unsafe_allow_html=True)
            st.markdown("<div class='apd-box'>", unsafe_allow_html=True)
            for a in d["apd"]:
                st.markdown(f"<div style='font-size:.88rem;color:#a0c4dc;margin-bottom:.3rem;'>{a}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='section-label' style='margin-top:1.2rem;'>Tindakan Darurat</div>", unsafe_allow_html=True)
            st.markdown("<div class='emergency-box'>", unsafe_allow_html=True)
            for e in d["darurat"]:
                st.markdown(f"<div style='font-size:.88rem;color:#e09090;margin-bottom:.4rem;'>{e}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='text-align:center;padding:3rem;color:#3a5a7a;'>
            <div style='font-size:3rem;margin-bottom:1rem;'>👆</div>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.2rem;font-weight:600;'>
                Pilih salah satu simbol GHS di atas
            </div>
            <p style='font-size:.9rem;'>untuk melihat informasi bahaya, APD, dan tindakan darurat.</p>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HALAMAN 3 – TENTANG APLIKASI
# ─────────────────────────────────────────────
elif menu == "ℹ️  Tentang Aplikasi":
    st.markdown("## ℹ️ Tentang Aplikasi")

    tab1, tab2, tab3 = st.tabs(["📖 Tentang", "📜 Regulasi", "👥 Tim Pengembang"])

    with tab1:
        st.markdown("""
        <div class='about-card'>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.3rem;font-weight:700;
                        color:#d0dce8;margin-bottom:.8rem;'>🔬 GHS B3 Identifier</div>
            <p>
                <b style='color:#a0b8cc;'>GHS B3 Identifier</b> adalah aplikasi berbasis web yang dikembangkan 
                untuk membantu tenaga kerja, ahli K3, laboran, dan masyarakat umum dalam memahami 
                simbol-simbol bahaya bahan kimia berbasis standar 
                <b style='color:#f0a500;'>Globally Harmonized System of Classification and Labelling of Chemicals (GHS)</b>.
            </p>
            <p>
                Aplikasi ini menyediakan informasi komprehensif meliputi deskripsi bahaya, 
                rekomendasi Alat Pelindung Diri (APD), panduan penyimpanan yang aman, 
                serta prosedur tindakan darurat yang sesuai dengan standar nasional 
                dan internasional yang berlaku.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class='about-card'>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;color:#d0dce8;
                            margin-bottom:.8rem;'>🎯 Tujuan Aplikasi</div>
                <ul style='padding-left:1.2rem;'>
                    <li>Meningkatkan kesadaran keselamatan kerja dalam penanganan B3</li>
                    <li>Memudahkan identifikasi bahaya bahan kimia secara cepat</li>
                    <li>Mendukung implementasi sistem GHS di Indonesia</li>
                    <li>Menyediakan referensi APD dan tindakan darurat yang terpercaya</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='about-card'>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;color:#d0dce8;
                            margin-bottom:.8rem;'>👥 Target Pengguna</div>
                <ul style='padding-left:1.2rem;'>
                    <li>Ahli K3 dan petugas keselamatan industri</li>
                    <li>Laboran dan peneliti laboratorium</li>
                    <li>Petugas pemadam kebakaran / HAZMAT</li>
                    <li>Mahasiswa teknik kimia dan kesehatan lingkungan</li>
                    <li>Masyarakat umum yang berinteraksi dengan B3</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='about-card'>
            <div style='font-family:Rajdhani,sans-serif;font-weight:700;color:#d0dce8;margin-bottom:.8rem;'>
                🔢 Nomor Darurat Penting
            </div>
        """, unsafe_allow_html=True)
        nums = [
            ("🚒", "113", "Pemadam Kebakaran"),
            ("🚑", "119", "Ambulans / Gawat Darurat"),
            ("🚨", "112", "Nomor Darurat Nasional"),
            ("🏛️", "021-500-454", "BNPB (Bencana Nasional)"),
            ("☢️", "021-570-2401", "BAPETEN (Nuklir)"),
            ("🌿", "021-8661-0011", "KLHK (Lingkungan)"),
        ]
        cols = st.columns(3)
        for i, (emoji, num, label) in enumerate(nums):
            with cols[i % 3]:
                st.markdown(f"""
                <div style='background:#0f1826;border:1px solid #1e3050;border-radius:10px;
                            padding:.8rem;text-align:center;margin-bottom:.5rem;'>
                    <div style='font-size:1.5rem;'>{emoji}</div>
                    <div style='font-family:IBM Plex Mono,monospace;font-size:1.1rem;
                                color:#f0a500;font-weight:600;'>{num}</div>
                    <div style='font-size:.75rem;color:#5a7a9a;margin-top:.2rem;'>{label}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class='about-card'>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.2rem;font-weight:700;
                        color:#d0dce8;margin-bottom:.8rem;'>📜 Landasan Regulasi</div>
            <p>Aplikasi ini dikembangkan dengan mengacu pada regulasi dan standar berikut:</p>
        </div>
        """, unsafe_allow_html=True)

        regulasi = [
            {
                "flag": "🇮🇩",
                "judul": "Peraturan Pemerintah No. 22 Tahun 2021",
                "tentang": "Penyelenggaraan Perlindungan dan Pengelolaan Lingkungan Hidup",
                "scope": "Mengatur pengelolaan Limbah B3 (Bahan Berbahaya dan Beracun) di Indonesia, termasuk klasifikasi, penyimpanan, pengangkutan, dan pembuangan.",
            },
            {
                "flag": "🇮🇩",
                "judul": "PermenLHK No. P.12/MENLHK/SETJEN/PLB.3/5/2020",
                "tentang": "Penyimpanan Limbah Bahan Berbahaya dan Beracun",
                "scope": "Mengatur teknis penyimpanan limbah B3 di fasilitas penghasil, termasuk desain TPS, label, dan simbol yang harus digunakan.",
            },
            {
                "flag": "🇮🇩",
                "judul": "PermenTenagaKerja No. 5 Tahun 2018",
                "tentang": "Keselamatan dan Kesehatan Kerja Lingkungan Kerja",
                "scope": "Mengatur standar lingkungan kerja, pengendalian hazard kimia, dan kewajiban penggunaan APD dalam penanganan bahan berbahaya.",
            },
            {
                "flag": "🌐",
                "judul": "GHS Rev. 10 (2023) — United Nations",
                "tentang": "Globally Harmonized System of Classification and Labelling of Chemicals",
                "scope": "Sistem harmonisasi global klasifikasi dan pelabelan bahan kimia yang menjadi basis simbol piktogram bahaya yang digunakan dalam aplikasi ini.",
            },
            {
                "flag": "🌐",
                "judul": "ISO 11014:2009",
                "tentang": "Safety data sheet for chemical products",
                "scope": "Standar internasional format dan isi Lembar Data Keselamatan (SDS/MSDS) untuk bahan kimia.",
            },
            {
                "flag": "🌐",
                "judul": "OSHA Hazard Communication Standard (29 CFR 1910.1200)",
                "tentang": "HazCom 2012 — Standar Komunikasi Bahaya OSHA",
                "scope": "Standar referensi internasional untuk komunikasi bahaya bahan kimia di tempat kerja, selaras dengan GHS.",
            },
        ]

        for r in regulasi:
            st.markdown(f"""
            <div class='about-card' style='border-left:4px solid #f0a500;'>
                <div style='display:flex;align-items:flex-start;gap:.8rem;'>
                    <span style='font-size:1.5rem;'>{r['flag']}</span>
                    <div>
                        <div style='font-family:Rajdhani,sans-serif;font-weight:700;
                                    color:#d0dce8;font-size:1rem;'>{r['judul']}</div>
                        <div style='font-size:.82rem;color:#f0a500;margin:.2rem 0;'>
                            {r['tentang']}
                        </div>
                        <p style='font-size:.84rem;margin:0;'>{r['scope']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div style='text-align:center;padding:1rem 0 1.5rem;'>
            <div style='font-family:Rajdhani,sans-serif;font-size:1.5rem;font-weight:700;
                        color:#d0dce8;'>Tim Pengembang Aplikasi</div>
            <p style='font-size:.9rem;margin:.3rem 0 0;'>
                Aplikasi ini dikembangkan oleh tim yang berkomitmen pada 
                peningkatan keselamatan kerja dan pengelolaan B3 di Indonesia.
            </p>
        </div>
        """, unsafe_allow_html=True)

        tim = [
            {
                "avatar": "👨‍💻",
                "nama": "Danapatti Arya Lazuardi",
                "nim": "2430552",
            },
            {
                "avatar": "👩‍🔬",
                "nama": "Daniswara Rizki",
                "nim": "2430553",
            },
            {
                "avatar": "👨‍🎨",
                "nama": "Faza Zain Ariq Athallah",
                "nim": "2430560",
            },
        ]

        cols = st.columns(3)
        for i, t in enumerate(tim):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class='team-card' style='margin-bottom:1rem;'>
                        <div style='font-size:2.5rem;margin-bottom:.5rem;'>{t['avatar']}</div>
                        <div style='font-family:Rajdhani,sans-serif;font-weight:700;
                            color:#d0dce8;font-size:1rem;line-height:1.3;
                            margin-bottom:.3rem;'>{t['nama']}</div>
                        <div style='font-size:.78rem;color:#f0a500;font-weight:600;
                            margin-bottom:.4rem;'>NIM: {t['nim']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class='about-card' style='text-align:center;'>
            <p style='font-size:.85rem;margin:0;'>
                🤝 <b style='color:#a0b8cc;'>Kolaborasi & Kontribusi:</b> 
                Kami menerima masukan, saran, dan kontribusi dari para ahli K3, 
                akademisi, dan praktisi industri untuk terus meningkatkan kualitas aplikasi ini.<br><br>
                📧 Hubungi kami: <span style='color:#f0a500;'>ghsb3identifier@k3indonesia.go.id</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
