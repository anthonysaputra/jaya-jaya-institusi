import streamlit as st
import pandas as pd
import joblib
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Jaya Jaya Student Insight",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# CUSTOM CSS
st.markdown("""
<style>
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 2.3rem;
    border-radius: 24px;
    border: 1px solid rgba(128,128,128,.20);
    margin-bottom: 1.5rem;
    background: linear-gradient(
        135deg,
        rgba(94, 53, 177, 0.12),
        rgba(63, 81, 181, 0.04)
    );
}
.hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: .3rem;
    letter-spacing: -1px;
}
.hero-subtitle {
    font-size: 1rem;
    opacity: .7;
    line-height: 1.6;
}
.section-title {
    font-size: 1.35rem;
    font-weight: 750;
    margin-top: 1.5rem;
    margin-bottom: .25rem;
}
.section-description {
    font-size: .9rem;
    opacity: .65;
    margin-bottom: 1rem;
}
.info-card {
    padding: 1rem 1.2rem;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,.18);
    margin-bottom: 1.5rem;
}
.result-card {
    padding: 2rem;
    border-radius: 22px;
    border: 1px solid rgba(128,128,128,.22);
    text-align: center;
    margin-top: 1rem;
}
.result-label {
    font-size: .85rem;
    opacity: .6;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.result-status {
    font-size: 2.5rem;
    font-weight: 850;
    margin-top: .4rem;
}
.footer {
    text-align: center;
    opacity: .45;
    font-size: .8rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# LOAD MODEL
@st.cache_resource
def load_model():
    model_path = "model/student_dropout_model.pkl"
    if not os.path.exists(model_path):
        return None
    return joblib.load(model_path)
model = load_model()

# CHECK MODEL
if model is None:
    st.error(
        "Model tidak ditemukan. Pastikan file "
        "`model/student_dropout_model.pkl` tersedia."
    )
    st.stop()

# MAPPING DATASET
# STATUS PERNIKAHAN
marital_options = {
    "Belum menikah": 1,
    "Menikah": 2,
    "Duda / janda": 3,
    "Bercerai": 4,
    "Hubungan facto": 5,
    "Pisah secara hukum": 6
}

# PROGRAM STUDI
course_options = {
    "Teknologi Produksi Biofuel": 33,
    "Desain Animasi dan Multimedia": 171,
    "Layanan Sosial (kelas malam)": 8014,
    "Agronomi": 9003,
    "Desain Komunikasi": 9070,
    "Keperawatan Veteriner": 9085,
    "Teknik Informatika": 9119,
    "Equinculture": 9130,
    "Manajemen": 9147,
    "Layanan Sosial": 9238,
    "Pariwisata": 9254,
    "Keperawatan": 9500,
    "Kebersihan Mulut": 9556,
    "Manajemen Periklanan dan Pemasaran": 9670,
    "Jurnalistik dan Komunikasi": 9773,
    "Pendidikan Dasar": 9853,
    "Manajemen (kelas malam)": 9991
}

# JALUR PENDAFTARAN
application_options = {
    "Pendaftaran umum - tahap pertama": 1,
    "Ordinance No. 612/93": 2,
    "Pendaftaran khusus - Azores": 5,
    "Lulusan pendidikan tinggi lainnya": 7,
    "Ordinance No. 854-B/99": 10,
    "Mahasiswa internasional": 15,
    "Pendaftaran khusus - Madeira": 16,
    "Pendaftaran umum - tahap kedua": 17,
    "Pendaftaran umum - tahap ketiga": 18,
    "Ordinance No. 533-A/99 - Different Plan": 26,
    "Ordinance No. 533-A/99 - Other Institution": 27,
    "Usia di atas 23 tahun": 39,
    "Mahasiswa transfer": 42,
    "Perubahan program studi": 43,
    "Pemegang diploma spesialisasi teknologi": 44,
    "Perubahan institusi / program studi": 51,
    "Pemegang diploma short cycle": 53,
    "Perubahan institusi / program studi internasional": 57
}

# PENDIDIKAN
qualification_options = {
    "Pendidikan menengah": 1,
    "Sarjana": 2,
    "Pendidikan tinggi - degree": 3,
    "Magister": 4,
    "Doktor": 5,
    "Pendidikan tinggi - frekuensi": 6,
    "Kelas 12 belum selesai": 9,
    "Kelas 11 belum selesai": 10,
    "Pendidikan kelas 11 lainnya": 12,
    "Kelas 10": 14,
    "Kelas 10 belum selesai": 15,
    "Pendidikan dasar tingkat 3": 19,
    "Pendidikan dasar tingkat 2": 38,
    "Kursus spesialisasi teknologi": 39,
    "Pendidikan tinggi - degree tingkat 1": 40,
    "Kursus teknis profesional tingkat tinggi": 42,
    "Pendidikan tinggi - magister tingkat 2": 43
}

# KEWARGANEGARAAN
nationality_options = {
    "Portugis": 1,
    "Jerman": 2,
    "Spanyol": 6,
    "Italia": 11,
    "Belanda": 13,
    "Inggris": 14,
    "Lithuania": 17,
    "Angola": 21,
    "Cape Verde": 22,
    "Guinea": 24,
    "Mozambik": 25,
    "São Tomé dan Príncipe": 26,
    "Turki": 32,
    "Brasil": 41,
    "Rumania": 62,
    "Moldova": 100,
    "Meksiko": 101,
    "Ukraina": 103,
    "Rusia": 105,
    "Kuba": 108,
    "Kolombia": 109
}

# HEADER
st.markdown("""
<div class="hero">
    <div class="hero-title">
        🎓 Jaya Jaya Student Insight
    </div>
    <div class="hero-subtitle">
        Sistem peringatan dini untuk membantu institusi
        memantau dan memahami status akademik mahasiswa.
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
<b>💡 Cara menggunakan aplikasi</b><br><br>
Masukkan informasi mahasiswa berdasarkan data yang tersedia.
Sistem akan memprediksi status mahasiswa menjadi
<b>Dropout</b>, <b>Enrolled</b>, atau <b>Graduate</b>.
Gunakan hasil prediksi sebagai bahan pendukung untuk
monitoring dan pemberian bimbingan.
</div>
""", unsafe_allow_html=True)
# FORM
with st.form("student_prediction_form"):
    # 1. PROFIL MAHASISWA
    st.markdown(
        '<div class="section-title">👤 Tentang Mahasiswa</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Informasi dasar mahasiswa.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input(
            "Berapa umur mahasiswa?",
            min_value=15,
            max_value=80,
            value=20,
            step=1,
            key="student_age"
        )
    with col2:
        gender_label = st.selectbox(
            "Jenis kelamin mahasiswa?",
            [
                "Perempuan",
                "Laki-laki"
            ],
            key="student_gender"
        )
        gender = (
            0
            if gender_label == "Perempuan"
            else 1
        )
    with col3:
        marital_label = st.selectbox(
            "Bagaimana status pernikahan mahasiswa?",
            list(marital_options.keys()),
            key="student_marital"
        )
        marital_status = marital_options[
            marital_label
        ]
    # 2. PENDIDIKAN & PENDAFTARAN
    st.markdown(
        '<div class="section-title">📚 Pendidikan & Pendaftaran</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Informasi pendidikan dan proses masuk mahasiswa.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        course_label = st.selectbox(
            "Program studi yang diambil?",
            list(course_options.keys()),
            key="student_course"
        )
        course = course_options[
            course_label
        ]
    with col2:
        application_label = st.selectbox(
            "Bagaimana mahasiswa masuk ke perguruan tinggi?",
            list(application_options.keys()),
            key="student_application_mode"
        )
        application_mode = application_options[
            application_label
        ]
    col1, col2, col3 = st.columns(3)
    with col1:
        previous_qualification_label = st.selectbox(
            "Pendidikan terakhir mahasiswa?",
            list(qualification_options.keys()),
            key="student_previous_qualification"
        )
        previous_qualification = qualification_options[
            previous_qualification_label
        ]
    with col2:
        previous_grade = st.number_input(
            "Berapa nilai pendidikan sebelumnya?",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            step=0.5,
            key="student_previous_grade"
        )
    with col3:
        admission_grade = st.number_input(
            "Berapa nilai mahasiswa saat masuk?",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            step=0.5,
            key="student_admission_grade"
        )

    # 3. PERFORMA SEMESTER 1
    st.markdown(
        '<div class="section-title">📖 Performa Semester 1</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Perkembangan akademik mahasiswa pada semester pertama.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        sem1_enrolled = st.number_input(
            "Berapa mata kuliah yang diambil?",
            min_value=0,
            max_value=30,
            value=5,
            step=1,
            key="main_sem1_enrolled"
        )
    with col2:
        sem1_approved = st.number_input(
            "Berapa mata kuliah yang berhasil lulus?",
            min_value=0,
            max_value=30,
            value=5,
            step=1,
            key="main_sem1_approved"
        )
    with col3:
        sem1_grade = st.number_input(
            "Berapa nilai rata-rata semester 1?",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.1,
            key="main_sem1_grade"
        )

    # 4. PERFORMA SEMESTER 2
    st.markdown(
        '<div class="section-title">📘 Performa Semester 2</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Perkembangan akademik terbaru mahasiswa.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        sem2_enrolled = st.number_input(
            "Berapa mata kuliah yang diambil?",
            min_value=0,
            max_value=30,
            value=5,
            step=1,
            key="main_sem2_enrolled"
        )
    with col2:
        sem2_approved = st.number_input(
            "Berapa mata kuliah yang berhasil lulus?",
            min_value=0,
            max_value=30,
            value=5,
            step=1,
            key="main_sem2_approved"
        )
    with col3:
        sem2_grade = st.number_input(
            "Berapa nilai rata-rata semester 2?",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.1,
            key="main_sem2_grade"
        )

    # 5. KONDISI FINANSIAL
    st.markdown(
        '<div class="section-title">💳 Kondisi Finansial</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Informasi mengenai pembayaran dan bantuan pendidikan.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        tuition_label = st.selectbox(
            "Apakah pembayaran kuliah sudah lancar?",
            [
                "Ya",
                "Belum"
            ],
            key="student_tuition"
        )
        tuition = (
            1
            if tuition_label == "Ya"
            else 0
        )
    with col2:
        debtor_label = st.selectbox(
            "Apakah mahasiswa memiliki tunggakan?",
            [
                "Tidak",
                "Ya"
            ],
            key="student_debtor"
        )
        debtor = (
            1
            if debtor_label == "Ya"
            else 0
        )
    with col3:
        scholarship_label = st.selectbox(
            "Apakah mahasiswa menerima beasiswa?",
            [
                "Tidak",
                "Ya"
            ],
            key="student_scholarship"
        )
        scholarship = (
            1
            if scholarship_label == "Ya"
            else 0
        )
    # 6. KONDISI LAIN
    st.markdown(
        '<div class="section-title">🌍 Kondisi Lain</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Informasi tambahan mengenai kondisi mahasiswa.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        attendance_label = st.selectbox(
            "Mahasiswa mengikuti kuliah pada waktu?",
            [
                "Siang",
                "Malam"
            ],
            key="student_attendance"
        )
        daytime = (
            1
            if attendance_label == "Siang"
            else 0
        )
    with col2:
        displaced_label = st.selectbox(
            "Apakah mahasiswa berasal dari luar wilayah sebelumnya?",
            [
                "Tidak",
                "Ya"
            ],
            key="student_displaced"
        )
        displaced = (
            1
            if displaced_label == "Ya"
            else 0
        )
    with col3:
        international_label = st.selectbox(
            "Apakah mahasiswa merupakan mahasiswa internasional?",
            [
                "Tidak",
                "Ya"
            ],
            key="student_international"
        )
        international = (
            1
            if international_label == "Ya"
            else 0
        )

    # 7. INFORMASI KELUARGA
    st.markdown(
        '<div class="section-title">👨‍👩‍👧 Informasi Keluarga</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-description">'
        'Informasi pendidikan orang tua mahasiswa.'
        '</div>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        mother_qualification_label = st.selectbox(
            "Pendidikan terakhir ibu?",
            list(qualification_options.keys()),
            key="mother_qualification"
        )
        mothers_qualification = qualification_options[
            mother_qualification_label
        ]
    with col2:
        father_qualification_label = st.selectbox(
            "Pendidikan terakhir ayah?",
            list(qualification_options.keys()),
            key="father_qualification"
        )
        fathers_qualification = qualification_options[
            father_qualification_label
        ]
        
    # 8. INFORMASI TAMBAHAN
    with st.expander("⚙️ Informasi tambahan"):

        st.caption(
            "Bagian ini berisi informasi yang lebih detail "
            "yang dibutuhkan oleh model."
        )
        # DATA PENDAFTARAN
        st.markdown("#### Detail pendaftaran")
        col1, col2, col3 = st.columns(3)
        with col1:
            application_order = st.number_input(
                "Program studi ini pilihan ke berapa?",
                min_value=0,
                max_value=9,
                value=1,
                step=1,
                key="additional_application_order"
            )
        with col2:
            nationality_label = st.selectbox(
                "Kewarganegaraan mahasiswa?",
                list(nationality_options.keys()),
                key="additional_nationality"
            )
            nationality = nationality_options[
                nationality_label
            ]
        with col3:
            special_needs_label = st.selectbox(
                "Apakah membutuhkan kebutuhan pendidikan khusus?",
                [
                    "Tidak",
                    "Ya"
                ],
                key="additional_special_needs"
            )
            special_needs = (
                1
                if special_needs_label == "Ya"
                else 0
            )

        # PEKERJAAN ORANG TUA
        st.markdown("#### Informasi pekerjaan orang tua")
        st.caption(
            "Pekerjaan orang tua pada dataset disimpan dalam "
            "bentuk kode kategori."
        )
        col1, col2 = st.columns(2)
        with col1:
            mothers_occupation = st.number_input(
                "Kode pekerjaan ibu",
                min_value=0,
                max_value=200,
                value=0,
                step=1,
                key="additional_mother_occupation"
            )
        with col2:
            fathers_occupation = st.number_input(
                "Kode pekerjaan ayah",
                min_value=0,
                max_value=200,
                value=0,
                step=1,
                key="additional_father_occupation"
            )

        # SEMESTER 1 TAMBAHAN
        st.markdown("#### Detail semester 1")
        col1, col2, col3 = st.columns(3)
        with col1:
            sem1_credited = st.number_input(
                "Mata kuliah yang dikonversi",
                min_value=0,
                max_value=30,
                value=0,
                step=1,
                key="additional_sem1_credited"
            )
        with col2:
            sem1_evaluations = st.number_input(
                "Mata kuliah yang dievaluasi",
                min_value=0,
                max_value=30,
                value=5,
                step=1,
                key="additional_sem1_evaluations"
            )
        with col3:
            sem1_without = st.number_input(
                "Mata kuliah tanpa evaluasi",
                min_value=0,
                max_value=30,
                value=0,
                step=1,
                key="additional_sem1_without"
            )
        # SEMESTER 2 TAMBAHAN
        st.markdown("#### Detail semester 2")
        col1, col2, col3 = st.columns(3)
        with col1:
            sem2_credited = st.number_input(
               "Mata kuliah yang dikonversi",
                min_value=0,
                max_value=30,
                value=0,
                step=1,
                key="additional_sem2_credited"
            )
        with col2:
           sem2_evaluations = st.number_input(
                "Mata kuliah yang dievaluasi",
                min_value=0,
                max_value=30,
                value=5,
                step=1,
                key="additional_sem2_evaluations"
            )
        with col3:
           sem2_without = st.number_input(
                "Mata kuliah tanpa evaluasi",
                min_value=0,
                max_value=30,
                value=0,
                step=1,
                key="additional_sem2_without"
            )
        # KONDISI EKONOMI
        st.markdown("#### Kondisi ekonomi")
        col1, col2, col3 = st.columns(3)
        with col1:
            unemployment = st.number_input(
                "Tingkat pengangguran",
                value=10.0,
                step=0.1,
                key="additional_unemployment"
            )
        with col2:
            inflation = st.number_input(
                "Tingkat inflasi",
                value=1.5,
                step=0.1,
                key="additional_inflation"
            )
        with col3:
            gdp = st.number_input(
                "GDP",
                value=1.5,
                step=0.1,
                key="additional_gdp"
            )
    # SUBMIT BUTTON
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button(
        "🔮 Prediksi Status Mahasiswa",
        use_container_width=True
    )
# PREDICTION
if submitted:
    # CREATE INPUT DATA
    input_data = pd.DataFrame([{
        "Marital_status":
            marital_status,
        "Application_mode":
            application_mode,
        "Application_order":
            application_order,
        "Course":
            course,
        "Daytime_evening_attendance":
            daytime,
        "Previous_qualification":
            previous_qualification,
        "Previous_qualification_grade":
            previous_grade,
        "Nacionality":
            nationality,
        "Mothers_qualification":
            mothers_qualification,
        "Fathers_qualification":
            fathers_qualification,
        "Mothers_occupation":
            mothers_occupation,
        "Fathers_occupation":
            fathers_occupation,
        "Admission_grade":
            admission_grade,
        "Displaced":
            displaced,
        "Educational_special_needs":
            special_needs,
        "Debtor":
            debtor,
        "Tuition_fees_up_to_date":
            tuition,
        "Gender":
            gender,
        "Scholarship_holder":
            scholarship,
        "International":
            international,
        "Age_at_enrollment":
            age,
            
        # SEMESTER 1
        "Curricular_units_1st_sem_credited":
            sem1_credited,
        "Curricular_units_1st_sem_enrolled":
            sem1_enrolled,
        "Curricular_units_1st_sem_evaluations":
            sem1_evaluations,
        "Curricular_units_1st_sem_approved":
            sem1_approved,
        "Curricular_units_1st_sem_grade":
            sem1_grade,
        "Curricular_units_1st_sem_without_evaluations":
            sem1_without,

        # SEMESTER 2
        "Curricular_units_2nd_sem_credited":
            sem2_credited,
        "Curricular_units_2nd_sem_enrolled":
            sem2_enrolled,
        "Curricular_units_2nd_sem_evaluations":
            sem2_evaluations,
        "Curricular_units_2nd_sem_approved":
            sem2_approved,
        "Curricular_units_2nd_sem_grade":
            sem2_grade,
        "Curricular_units_2nd_sem_without_evaluations":
            sem2_without,

        # ECONOMIC
        "Unemployment_rate":
            unemployment,
        "Inflation_rate":
            inflation,
        "GDP":
            gdp
    }])

    # MODEL PREDICTION
    try:
        prediction = model.predict(
            input_data
        )[0]
        probabilities = model.predict_proba(
            input_data
        )[0]
        classes = model.classes_
    except Exception as e:
        st.error(
            "Terjadi masalah saat melakukan prediksi."
        )
        st.code(str(e))
        st.stop()

    # RESULT
    st.markdown("---")
    st.markdown("## 🎯 Hasil Prediksi")

    # DROPOUT
    if prediction == "Dropout":
        st.markdown("""
        <div class="result-card">
            <div class="result-label">
                Status yang diprediksi
            </div>
            <div class="result-status">
                ⚠️ DROPOUT
            </div>
            <p>
                Mahasiswa memiliki karakteristik yang
                diprediksi mengarah pada status dropout.
            </p>

        </div>
        """, unsafe_allow_html=True)
        st.warning(
            "💡 **Perlu perhatian lebih.** "
            "Hasil ini dapat digunakan sebagai sinyal awal "
            "untuk monitoring dan pendampingan mahasiswa."
        )
        
    # ENROLLED
    elif prediction == "Enrolled":
        st.markdown("""
        <div class="result-card">
            <div class="result-label">
                Status yang diprediksi
            </div>
            <div class="result-status">
                📚 ENROLLED
            </div>
            <p>
                Mahasiswa memiliki karakteristik yang
                diprediksi masih berada dalam status enrolled.
            </p>

        </div>
        """, unsafe_allow_html=True)

        st.info(
            "💡 Tetap lakukan monitoring terhadap "
            "perkembangan akademik mahasiswa."
        )

    # GRADUATE
    else:
        st.markdown("""
        <div class="result-card">
            <div class="result-label">
                Status yang diprediksi
            </div>
            <div class="result-status">
                🎓 GRADUATE
            </div>
            <p>
                Mahasiswa memiliki karakteristik yang
                diprediksi mengarah pada status graduate.
            </p>

        </div>
        """, unsafe_allow_html=True)
        st.success(
            "💡 Performa mahasiswa menunjukkan karakteristik "
            "yang mendukung keberhasilan akademik."
        )

    # PROBABILITY
    st.markdown("### 📊 Tingkat Keyakinan Model")
    probability_df = pd.DataFrame({
        "Status":
            classes,
        "Probabilitas":
            probabilities
    })
    probability_df["Persentase"] = (
        probability_df["Probabilitas"] * 100
    ).round(1)

    # KPI
    cols = st.columns(
        len(probability_df)
    )
    for col, (_, row) in zip(
        cols,
        probability_df.iterrows()
    ):
        with col:
            st.metric(
                label=row["Status"],
                value=f"{row['Persentase']:.1f}%"
            )
    # Chart
    st.bar_chart(
        probability_df.set_index(
            "Status"
        )["Probabilitas"]
    )
    # RECOMMENDATION
    st.markdown("### 💡 Rekomendasi Tindakan")
    if prediction == "Dropout":
        st.error("""
**Prioritas pendampingan: TINGGI**
- Pantau perkembangan akademik secara berkala.
- Perhatikan jumlah mata kuliah yang berhasil diselesaikan.
- Evaluasi kemungkinan kendala finansial.
- Pertimbangkan bimbingan akademik atau konseling.""")
    elif prediction == "Enrolled":
        st.info(""" **Prioritas pendampingan: SEDANG**
- Pantau perkembangan akademik.
- Perhatikan perubahan nilai dan jumlah mata kuliah yang lulus.
- Berikan dukungan apabila terjadi penurunan performa.""")
    else:
        st.success("""
**Prioritas pendampingan: RENDAH**
- Pertahankan performa akademik.
- Berikan apresiasi terhadap perkembangan mahasiswa.
- Tetap lakukan monitoring secara berkala.""")

    # DISCLAIMER
    st.markdown("---")
    st.caption(
        "⚠️ Prediksi model merupakan alat bantu pengambilan "
        "keputusan, bukan keputusan final mengenai status mahasiswa."
    )
# FOOTER
st.markdown("""
<div class="footer">
Jaya Jaya Student Insight · Machine Learning Prototype
</div>
""", unsafe_allow_html=True)