<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"/>
  <title>Return-It Warehouse Operations</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
  <style>
    @layer base { 
      html, body { width: 100vw; margin: 0; padding: 0; min-height: 100%; } 
      body { overscroll-behavior-y: none; } 
      .pb-safe { padding-bottom: env(safe-area-inset-bottom, 0px); } 
      .pt-safe { padding-top: env(safe-area-inset-top, 0px); } 
      main > :first-child { margin-top: 0 !important; } 
      main > :last-child { margin-bottom: 0 !important; } 
    } 
    ::-webkit-scrollbar { display: none; } 
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    body { min-height: max(884px, 100dvh); }
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = { 
      darkMode: "class", 
      theme: { 
        extend: { 
          colors: { 
            "on-primary-container": "#7c839b", "on-secondary-fixed-variant": "#003ea8", "outline-variant": "#c6c6cd", "on-error": "#ffffff", "error": "#ba1a1a", "primary-fixed": "#dae2fd", "on-secondary-container": "#fefcff", "secondary-container": "#316bf3", "surface-container-lowest": "#ffffff", "on-tertiary": "#ffffff", "tertiary-container": "#002113", "inverse-primary": "#bec6e0", "secondary": "#0051d5", "on-error-container": "#93000a", "inverse-surface": "#213145", "primary": "#000000", "surface-container": "#e5eeff", "error-container": "#ffdad6", "on-tertiary-container": "#009668", "on-tertiary-fixed-variant": "#005236", "primary-container": "#131b2e", "surface-container-high": "#dce9ff", "on-secondary": "#ffffff", "on-primary-fixed-variant": "#3f465c", "on-background": "#0b1c30", "on-surface-variant": "#45464d", "surface-bright": "#f8f9ff", "surface-dim": "#cbdbf5", "surface-variant": "#d3e4fe", "on-surface": "#0b1c30", "surface-container-highest": "#d3e4fe", "secondary-fixed": "#dbe1ff", "tertiary-fixed": "#6ffbbe", "surface": "#f8f9ff", "primary-fixed-dim": "#bec6e0", "on-primary-fixed": "#131b2e", "secondary-fixed-dim": "#b4c5ff", "on-tertiary-fixed": "#002113", "tertiary": "#000000", "outline": "#76777d", "inverse-on-surface": "#eaf1ff", "surface-tint": "#565e74", "tertiary-fixed-dim": "#4edea3", "surface-container-low": "#eff4ff", "on-primary": "#ffffff" 
          }, 
          borderRadius: { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, 
          spacing: { "margin-desktop": "2rem", "gutter-desktop": "1.5rem", "space-md": "0.75rem", "space-lg": "1rem", "margin": "1rem", "gutter": "1rem", "space-xl": "1.5rem", "space-xs": "0.25rem", "space-sm": "0.5rem" }, 
          fontFamily: { 
            "label-code": ["JetBrains Mono"], "metric-value": ["Inter"], "label-ui": ["Inter"], "body-lg": ["Inter"], "display-lg": ["Inter"], "headline-md": ["Inter"], "headline-lg": ["Inter"], "headline-sm": ["Inter"], "body-md": ["Inter"], "display-lg-mobile": ["Inter"], "body-sm": ["Inter"] 
          } 
        } 
      } 
    };
  </script>
</head>
<body class="bg-surface text-on-surface font-body-md text-body-md min-h-screen flex flex-col selection:bg-secondary-fixed">
  
  <!-- Header -->
  <header class="fixed top-0 w-full z-50 pt-safe bg-surface/90 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
    <div class="h-28 px-margin flex flex-col justify-between py-space-sm">
      <div class="flex items-center justify-between gap-space-sm">
        <div class="flex items-center gap-space-sm min-w-0">
          <img alt="Return-It Operations Logo" class="h-8 w-auto object-contain" src="https://lh3.googleusercontent.com/aida/AEtjO1VzOkdZpBTKu8oglRxa_RCBsJcK_feFLhys90BGPCHPNWXhIzmNp9hp-VpkW3XMxSKf3pq_1m8x467JNd3TFGK20Ew5TmiA4-lWOY2SkLX8Tfql0L_FMWr3qxPhuGyVHh1vn_kUzHGZeXk1ZMbz16PnRSaRk56w9SvJZhJEnHNh1h4SB_FrVx5esNA8AauChvavcjIQdo4WuAUXs8QYJWHlYzhB0YJ6UfX4fsO0Gi0v52coiZsPLH1qss-Q"/>
          <div class="flex flex-col min-w-0">
            <div class="flex items-center gap-space-xs">
              <span class="font-headline-sm text-headline-sm text-on-surface tracking-tight truncate">Operations KPI</span>
              <span class="font-label-code text-label-code px-space-xs py-0.5 rounded bg-surface-container-high text-secondary font-medium hidden sm:inline-block">WH-04</span>
            </div>
            <span class="font-label-ui text-label-ui text-on-surface-variant uppercase tracking-wider flex items-center gap-space-xs">
              <span class="w-1.5 h-1.5 rounded-full bg-secondary animate-pulse inline-block"></span>LIVE 14:32:08 UTC
            </span>
          </div>
        </div>
        <div class="flex items-center gap-space-xs">
          <button aria-label="Notifications" class="relative w-11 h-11 flex items-center justify-center rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container-low transition-colors" type="button">
            <span class="material-symbols-outlined text-[22px]">notifications</span>
            <span class="absolute top-2 right-2 flex items-center justify-center min-w-[16px] h-4 px-1 text-[10px] font-bold leading-none text-on-error bg-error rounded-full ring-2 ring-surface">3</span>
          </button>
          <div class="flex items-center gap-space-xs pl-space-xs">
            <div class="text-right hidden sm:flex flex-col">
              <span class="font-label-ui text-label-ui text-on-surface font-semibold">Sajad Taheri</span>
              <span class="font-label-code text-label-code text-on-surface-variant text-[10px]">Administrator</span>
            </div>
            <img alt="Profile" class="w-8 h-8 rounded-full object-cover ring-1 ring-outline-variant/30" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAyHHddXgX-iZr7ceHGtbBNgqM_c8P00p27oWhieRTOAoKqSxtm5dzAahTGcjFjhtxClmVHofeQ96R-ayrAXz_SluRggmxSQdv0XvwcWshV42pzBMAJjn6SJbRxcHn2_TnhLe0mLU6u5x2xrvtHDqLNcqnkDsKQv_gmvoeOqfodo9I6AoYT9UvlTeog8-HzzUBuVI81zL15tKXtd5CeTrrkkj0DbAGU78FU-c0nTh67hPCTZHoDgKOzmw"/>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-space-sm pt-space-xs">
        <div class="relative flex-1 flex items-center">
          <span class="material-symbols-outlined absolute left-3 text-on-surface-variant text-[18px] pointer-events-none">search</span>
          <input class="w-full h-9 pl-9 pr-3 rounded bg-surface-container-lowest text-on-surface placeholder:text-on-surface-variant font-body-sm text-body-sm focus:outline-none focus:ring-1 focus:ring-secondary" placeholder="Search associates, paths, SKU, logs..." type="search"/>
          <span class="font-label-code text-label-code absolute right-2.5 text-on-surface-variant/70 text-[10px] hidden sm:block">⌘K</span>
        </div>
        <button aria-label="Filter Table" class="h-9 px-space-sm rounded bg-surface-container-low hover:bg-surface-container text-on-surface font-label-ui text-label-ui flex items-center gap-1 transition-colors" type="button">
          <span class="material-symbols-outlined text-[18px] text-secondary">tune</span>
          <span class="hidden xs:inline">Filter</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="flex flex-col relative w-full pt-28 pb-24 bg-surface min-h-screen">
    <div class="flex flex-col w-full px-margin py-space-md gap-space-lg">
      
      <!-- Operational Header -->
      <div class="flex flex-col gap-space-xs">
        <div class="flex items-center justify-between">
          <span class="font-label-ui text-label-ui text-secondary uppercase tracking-wider font-semibold">Distribution Hub 04</span>
          <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-surface-container-high text-on-surface text-[11px] font-label-code">
            <span class="w-1.5 h-1.5 rounded-full bg-on-tertiary-container animate-ping"></span>
            SYNC 14:15 PST
          </span>
        </div>
        <h1 class="font-headline-md text-headline-md text-on-surface tracking-tight">Warehouse KPI & Floor Flow</h1>
        <p class="font-body-sm text-body-sm text-on-surface-variant flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px] text-secondary">schedule</span>
          Shift A (06:00 - 14:30) • Primary Material Sort
        </p>
      </div>

      <!-- KPI Metrics Carousel Track -->
      <div class="flex flex-col gap-space-xs">
        <div class="flex items-center justify-between">
          <span class="font-label-ui text-label-ui text-on-surface-variant uppercase tracking-wider">Operational Velocity</span>
          <span class="font-label-code text-label-code text-on-surface-variant/80">7 Key Indices</span>
        </div>
        <div class="flex gap-space-sm overflow-x-auto no-scrollbar pb-1 -mx-margin px-margin snap-x snap-mandatory">
          <!-- Card 1 -->
          <div class="snap-start shrink-0 w-44 p-space-md rounded-xl bg-surface-container-lowest shadow-sm flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="p-1.5 rounded bg-surface-container text-secondary flex items-center justify-center">
                <span class="material-symbols-outlined text-[18px]">inventory_2</span>
              </span>
              <span class="px-1.5 py-0.5 rounded-full bg-tertiary-fixed text-on-tertiary-fixed font-label-ui text-[10px] font-bold">+12.4%</span>
            </div>
            <div class="mt-space-md">
              <div class="font-metric-value text-[24px] leading-7 font-bold text-on-surface">48,920</div>
              <div class="font-label-ui text-label-ui text-on-surface-variant uppercase mt-1">Total Processed</div>
            </div>
            <div class="mt-2 w-full bg-surface-container-high rounded-full h-1">
              <div class="bg-secondary h-1 rounded-full w-[84%]"></div>
            </div>
          </div>
          <!-- Card 2 -->
          <div class="snap-start shrink-0 w-44 p-space-md rounded-xl bg-surface-container-lowest shadow-sm flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="p-1.5 rounded bg-surface-container text-secondary flex items-center justify-center">
                <span class="material-symbols-outlined text-[18px]">speed</span>
              </span>
              <span class="px-1.5 py-0.5 rounded-full bg-tertiary-fixed text-on-tertiary-fixed font-label-ui text-[10px] font-bold">+6.2%</span>
            </div>
            <div class="mt-space-md">
              <div class="font-metric-value text-[24px] leading-7 font-bold text-on-surface">284 <span class="text-sm font-normal text-on-surface-variant">UPH</span></div>
              <div class="font-label-ui text-label-ui text-on-surface-variant uppercase mt-1">Average Flow Rate</div>
            </div>
            <div class="mt-2 text-[10px] font-label-code text-on-surface-variant">Target: 260 UPH</div>
          </div>
          <!-- Card 3 -->
          <div class="snap-start shrink-0 w-44 p-space-md rounded-xl bg-surface-container-lowest shadow-sm flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="p-1.5 rounded bg-surface-container text-secondary flex items-center justify-center">
                <span class="material-symbols-outlined text-[18px]">group</span>
              </span>
              <span class="px-1.5 py-0.5 rounded-full bg-secondary-fixed text-on-secondary-fixed-variant font-label-ui text-[10px] font-bold">93.3%</span>
            </div>
            <div class="mt-space-md">
              <div class="font-metric-value text-[24px] leading-7 font-bold text-on-surface">42 <span class="text-sm font-normal text-on-surface-variant">/ 45</span></div>
              <div class="font-label-ui text-label-ui text-on-surface-variant uppercase mt-1">On Floor Staff</div>
            </div>
            <div class="mt-2 text-[10px] font-label-code text-on-surface-variant">3 On Scheduled Break</div>
          </div>
          <!-- Card 4 -->
          <div class="snap-start shrink-0 w-44 p-space-md rounded-xl bg-surface-container-lowest shadow-sm flex flex-col justify-between">
            <div class="flex items-center justify-between">
              <span class="p-1.5 rounded bg-surface-container text-secondary flex items-center justify-center">
                <span class="material-symbols-outlined text-[18px]">verified</span>
              </span>
              <span class="px-1.5 py-0.5 rounded-full bg-tertiary-fixed text-on-tertiary-fixed font-label-ui text-[10px] font-bold">SLA Near</span>
            </div>
            <div class="mt-space-md">
              <div class="font-metric-value text-[24px] leading-7 font-bold text-on-surface">98.4%</div>
              <div class="font-label-ui text-label-ui text-on-surface-variant uppercase mt-1">Efficiency Target</div>
            </div>
            <div class="mt-2 text-[10px] font-label-code text-on-surface-variant">Target SLA: 99.0%</div>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- Bottom Navigation -->
  <nav class="fixed bottom-0 w-full z-50 pb-safe bg-surface-container-lowest/95 backdrop-blur-xl shadow-[0_-2px_12px_rgba(0,0,0,0.06)]">
    <div class="flex items-center justify-around h-16 px-space-xs overflow-x-auto no-scrollbar">
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 transition-colors text-secondary border-t-2 border-secondary font-semibold" href="#">
        <span class="material-symbols-outlined text-[20px]">dashboard</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Dashboard</span>
      </a>
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 text-on-surface-variant hover:text-on-surface transition-colors" href="#">
        <span class="material-symbols-outlined text-[20px]">group</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Associates</span>
      </a>
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 text-on-surface-variant hover:text-on-surface transition-colors" href="#">
        <span class="material-symbols-outlined text-[20px]">alt_route</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Process Paths</span>
      </a>
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 text-on-surface-variant hover:text-on-surface transition-colors" href="#">
        <span class="material-symbols-outlined text-[20px]">insights</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Reports</span>
      </a>
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 text-on-surface-variant hover:text-on-surface transition-colors" href="#">
        <span class="material-symbols-outlined text-[20px]">receipt_long</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Logs</span>
      </a>
      <a class="flex flex-col items-center justify-center min-w-[56px] h-full gap-0.5 text-on-surface-variant hover:text-on-surface transition-colors" href="#">
        <span class="material-symbols-outlined text-[20px]">settings</span>
        <span class="font-label-ui text-[10px] tracking-tight text-center truncate">Settings</span>
      </a>
    </div>
  </nav>

</body>
</html>