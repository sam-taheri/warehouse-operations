import pandas as pd
import streamlit as st

# تنظیمات صفحه
st.set_page_config(
    page_title="Operations KPI - WH-04", page_icon="📊", layout="wide"
)

# سایدبار و ناوبری
st.sidebar.image("https://img.icons8.com/color/96/warehouse.png", width=50)
st.sidebar.title("Warehouse OS (WH-04)")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard (Counts & Audits)",
        "Monthly Reports & Analytics",
        "Upload Shift Report",
    ],
)

# هدر صفحه اصلی
st.title("Operations KPI & Floor Flow")
st.markdown(
    "**Distribution Hub 04** | Integrated Counts & Audit Management Hub"
)
st.markdown("---")

if menu == "Dashboard (Counts & Audits)":

    # تب‌بندی اصلی برای دسترسی سریع به Counts و Audits
    main_tab1, main_tab2 = st.tabs(
        ["📊 KPI Counts (POR, TOMRA, MX)", "🛡️ Audit Section"]
    )

    # ----------------------------------------------------
    # تب اول: بخش Counts (شاخص‌های اصلی عملکرد خطوط)
    # ----------------------------------------------------
    with main_tab1:
        st.subheader("📈 Core KPI Counts & Live Pathways")

        # کارت‌های آماری بالایی
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric(
                "Total Processed (This Month)",
                "48,920 Plts",
                "+12.4% vs last",
            )
        with c2:
            st.metric("POR Inbound", "18,400 Units", "38% share")
        with c3:
            st.metric("TOMRA Systems", "22,100 Units", "45% share")
        with c4:
            st.metric("MachineX HS", "8,420 Units", "17% share")

        st.markdown("### Active Associate Performance (Counts)")
        data_kpi = {
            "Associate Name": [
                "Sajad Taheri",
                "Cynthia",
                "Jalpreet",
                "Danielle",
                "Navin Sami",
            ],
            "Process Path": [
                "TOMRA Systems",
                "POR Inbound",
                "TOMRA Systems",
                "MachineX",
                "POR Inbound",
            ],
            "Qty Processed": [1420, 1240, 980, 1450, 1120],
            "Rate (UPH)": ["284 UPH", "165 UPH", "145 UPH", "181 UPH", "154 UPH"],
            "Status": ["Optimal", "Active", "Active", "Break", "Active"],
        }
        st.dataframe(pd.DataFrame(data_kpi), use_container_width=True)

    # ----------------------------------------------------
    # تب دوم: بخش Audit (شامل Big Bag و TOMRA Audit)
    # ----------------------------------------------------
    with main_tab2:
        st.subheader("🛡️ Audit Management & Compliance")

        audit_sub1, audit_sub2 = st.tabs(
            ["📦 Big Bag Station Audit", "🔄 TOMRA Audit"]
        )

        with audit_sub1:
            st.markdown("### Big Bag Station Audit Logs")
            big_bag_data = {
                "Audit ID": ["AUD-BB-01", "AUD-BB-02", "AUD-BB-03"],
                "Station": ["Station A-1", "Station A-2", "Station B-1"],
                "Inspector": ["Sajad Taheri", "Navin Sami", "Cynthia"],
                "Status": [
                    "Pending Sign-off",
                    "Approved",
                    "Requires Maintenance",
                ],
                "Date": ["2026-09-17", "2026-09-16", "2026-09-15"],
            }
            st.dataframe(
                pd.DataFrame(big_bag_data), use_container_width=True
            )

        with audit_sub2:
            st.markdown("### TOMRA System Audits")
            tomra_audit_data = {
                "Audit ID": ["AUD-TOM-101", "AUD-TOM-102"],
                "Line Number": ["TOMRA Line 1", "TOMRA Line 3"],
                "Error Rate": ["0.1%", "0.4%"],
                "Compliance": ["Passed", "Passed"],
                "Sign-off By": ["Sajad Taheri", "Manager"],
            }
            st.dataframe(
                pd.DataFrame(tomra_audit_data), use_container_width=True
            )

# ----------------------------------------------------
# بخش گزارش‌های ماهانه
# ----------------------------------------------------
elif menu == "Monthly Reports & Analytics":
    st.subheader("📊 Monthly Performance & Statistical Reports")
    m1, m2 = st.columns(2)
    with m1:
        st.info("📅 **Current Month Summary (September 2026)**")
        st.metric("Total Warehouse Volume", "142,500 Units")
    with m2:
        st.success("✅ **SLA & Efficiency Target**")
        st.metric("Audit Compliance Rate", "98.5%")

    st.markdown("---")
    st.download_button(
        label="📥 Download Full Monthly Report (CSV)",
        data="Sample,Monthly,Data",
        file_name="Warehouse_Monthly_Report_Sep2026.csv",
        mime="text/csv",
    )

# ----------------------------------------------------
# بخش آپلود گزارش
# ----------------------------------------------------
elif menu == "Upload Shift Report":
    st.subheader("📂 Ingestion Hub: Upload Shift Reports")
    uploaded_file = st.file_uploader(
        "Upload daily PDF/Excel report", type=["pdf", "xlsx", "csv"]
    )
    if uploaded_file:
        st.success("File uploaded successfully!")