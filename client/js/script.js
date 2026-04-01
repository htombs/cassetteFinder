// ── CONFIG ──
const API_URL = "http://localhost:5000";

// ── STATE ──
let allCassettes = []; // full dataset loaded once on page load
let filtered = []; // currently displayed subset
let sortCol = null;
let sortDir = 1; // 1 = asc, -1 = desc

// Speed → ratio mapping built from the live data.
// Used to cascade the ratio dropdown when a speed is selected.
const ratiosBySpeed = {};

// ── DOM REFS ──
const output = document.getElementById("output");
const mobileCards = document.getElementById("mobile-cards");
const resultCount = document.getElementById("result-count");
const filterChips = document.getElementById("filter-chips");
const emptyState = document.getElementById("empty-state");
const loadingState = document.getElementById("loading-state");
const searchInput = document.getElementById("search-input");
const speedSelect = document.getElementById("speed-select");
const ratioSelect = document.getElementById("ratio-select");
const brandSelect = document.getElementById("brand-select");
const btnReset = document.getElementById("btn-reset");
const btnResetEmpty = document.getElementById("btn-reset-empty");
const scrollBtn = document.getElementById("scrollToTopBtn");

// ── INITIAL DATA LOAD ──
// Fetch all cassettes once; all filtering is then done client-side
// so the page feels instant with no submit button required.
function loadAllCassettes() {
  showLoading(true);

  fetch(`${API_URL}/all`)
    .then((res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then((data) => {
      allCassettes = data;
      buildRatioMap();
      buildBrandDropdown();
      showLoading(false);
      applyFilters();
    })
    .catch((err) => {
      console.error("Failed to load cassettes:", err);
      showLoading(false);
      resultCount.innerHTML = "Could not load data — is the API running?";
    });
}

// Build a lookup of { speed: [ratio, ratio, …] } from the live data
function buildRatioMap() {
  allCassettes.forEach((item) => {
    const spd = String(item.speed);
    if (!ratiosBySpeed[spd]) ratiosBySpeed[spd] = new Set();
    ratiosBySpeed[spd].add(item.ratio);
  });
  // Convert sets to sorted arrays
  for (const spd in ratiosBySpeed) {
    ratiosBySpeed[spd] = [...ratiosBySpeed[spd]].sort(ratioSort);
  }
  updateRatioDropdown();
}

// Build brand dropdown from live data (removes any brands not actually in the DB)
function buildBrandDropdown() {
  const brands = [...new Set(allCassettes.map((c) => c.brand))].sort();
  brandSelect.innerHTML = '<option value="">All brands</option>';
  brands.forEach((b) => {
    const opt = document.createElement("option");
    opt.value = b;
    opt.textContent = b;
    brandSelect.appendChild(opt);
  });
}

// ── RATIO DROPDOWN — grouped by small sprocket ──
// Replaces the flat 50+ option list with optgroups like "10-tooth", "11-tooth" etc.
function updateRatioDropdown() {
  const selectedSpeed = speedSelect.value;
  const currentRatio = ratioSelect.value;

  // Which ratios to show: only those valid for the selected speed, or all
  let ratios;
  if (selectedSpeed && ratiosBySpeed[selectedSpeed]) {
    ratios = ratiosBySpeed[selectedSpeed];
  } else {
    const all = new Set();
    allCassettes.forEach((c) => all.add(c.ratio));
    ratios = [...all].sort(ratioSort);
  }

  // Group by small sprocket (e.g. "10", "11", "12" …)
  const groups = {};
  ratios.forEach((r) => {
    const small = r.split("-")[0];
    if (!groups[small]) groups[small] = [];
    groups[small].push(r);
  });

  ratioSelect.innerHTML = '<option value="">All ratios</option>';
  Object.keys(groups)
    .sort((a, b) => Number(a) - Number(b))
    .forEach((small) => {
      const grp = document.createElement("optgroup");
      grp.label = `${small}-tooth small sprocket`;
      groups[small].forEach((r) => {
        const opt = document.createElement("option");
        opt.value = r;
        opt.textContent = r;
        if (r === currentRatio) opt.selected = true;
        grp.appendChild(opt);
      });
      ratioSelect.appendChild(grp);
    });
}

// Sort ratios numerically by small then large sprocket
function ratioSort(a, b) {
  const [as, al] = a.split("-").map(Number);
  const [bs, bl] = b.split("-").map(Number);
  return as !== bs ? as - bs : al - bl;
}

// ── FILTERING ──
function getFilters() {
  return {
    search: searchInput.value.trim().toLowerCase(),
    speed: speedSelect.value,
    ratio: ratioSelect.value,
    brand: brandSelect.value,
  };
}

function applyFilters() {
  const f = getFilters();

  filtered = allCassettes.filter((item) => {
    if (f.speed && String(item.speed) !== f.speed) return false;
    if (f.ratio && item.ratio !== f.ratio) return false;
    if (f.brand && item.brand !== f.brand) return false;
    if (f.search) {
      const hay =
        `${item.brand} ${item.model} ${item.part_number} ${item.ratio}`.toLowerCase();
      if (!hay.includes(f.search)) return false;
    }
    return true;
  });

  if (sortCol) {
    filtered.sort((a, b) => {
      let av = a[sortCol],
        bv = b[sortCol];
      if (sortCol === "speed" || sortCol === "rrp") {
        av = Number(av);
        bv = Number(bv);
      } else {
        av = String(av).toLowerCase();
        bv = String(bv).toLowerCase();
      }
      return av < bv ? -sortDir : av > bv ? sortDir : 0;
    });
  }

  // Cascade: keep ratio dropdown in sync with selected speed
  updateRatioDropdown();

  // Mark filters as active
  searchInput.classList.toggle("is-active", !!f.search);
  speedSelect.classList.toggle("is-active", !!f.speed);
  ratioSelect.classList.toggle("is-active", !!f.ratio);
  brandSelect.classList.toggle("is-active", !!f.brand);

  renderTable();
  renderCards();
  renderStatus(f);
}

// ── RENDER — TABLE (desktop) ──
function renderTable() {
  if (filtered.length === 0) {
    output.innerHTML = "";
    emptyState.classList.add("visible");
    return;
  }
  emptyState.classList.remove("visible");

  output.innerHTML = filtered
    .map(
      (item) => `
        <tr>
            <td><strong>${item.brand}</strong></td>
            <td>${item.model || "—"}</td>
            <td><span class="badge-speed">${item.speed}spd</span></td>
            <td><span class="badge-ratio">${item.ratio}</span></td>
            <td><span class="part-num">${item.part_number}</span></td>
            <td>£${Number(item.rrp).toFixed(2)}</td>
            <td>${item.distributor}</td>
            <td>${
              item.link
                ? `<a class="b2b-link" href="${item.link}" target="_blank" rel="noopener">
                       ${item.distributor} ↗
                   </a>`
                : "—"
            }</td>
        </tr>
    `,
    )
    .join("");
}

// ── RENDER — MOBILE CARDS ──
function renderCards() {
  if (filtered.length === 0) {
    mobileCards.innerHTML = "";
    return;
  }

  mobileCards.innerHTML = filtered
    .map(
      (item) => `
        <div class="mobile-card">
            <div class="card-header">
                <div class="card-brand">${item.brand}</div>
                <div class="card-model">${item.model || "—"}</div>
            </div>
            <div class="card-field">
                <span class="card-label">Speed</span>
                <span class="card-value">${item.speed} speed</span>
            </div>
            <div class="card-field">
                <span class="card-label">Ratio</span>
                <span class="card-value">${item.ratio}</span>
            </div>
            <div class="card-field">
                <span class="card-label">Part No.</span>
                <span class="card-value" style="font-family:monospace;font-size:0.8rem">${item.part_number}</span>
            </div>
            <div class="card-field">
                <span class="card-label">Price</span>
                <span class="card-value">£${Number(item.rrp).toFixed(2)}</span>
            </div>
            <div class="card-field">
                <span class="card-label">Distributor</span>
                <span class="card-value">${item.distributor}</span>
            </div>
            <div class="card-field" style="grid-column: 1 / -1">
                <span class="card-label">B2B Link</span>
                <span class="card-value">
                    ${
                      item.link
                        ? `<a class="b2b-link" href="${item.link}" target="_blank" rel="noopener">${item.distributor} ↗</a>`
                        : "—"
                    }
                </span>
            </div>
        </div>
    `,
    )
    .join("");
}

// ── RENDER — STATUS BAR ──
function renderStatus(f) {
  resultCount.innerHTML = `<strong>${filtered.length}</strong> of ${allCassettes.length} cassettes`;

  const chips = [];
  if (f.search) chips.push(`"${f.search}"`);
  if (f.speed) chips.push(`${f.speed} speed`);
  if (f.ratio) chips.push(f.ratio);
  if (f.brand) chips.push(f.brand);

  filterChips.innerHTML = chips
    .map((c) => `<span class="chip">${c}</span>`)
    .join("");
}

// ── LOADING STATE ──
function showLoading(show) {
  loadingState.classList.toggle("visible", show);
}

// ── SORT — clicking a <th> sorts by that column ──
document.querySelectorAll("th[data-col]").forEach((th) => {
  th.addEventListener("click", () => {
    const col = th.dataset.col;
    if (sortCol === col) {
      sortDir *= -1;
    } else {
      sortCol = col;
      sortDir = 1;
    }

    // Update sort icons
    document.querySelectorAll("th[data-col]").forEach((t) => {
      t.classList.remove("sorted");
      const ico = t.querySelector(".sort-icon");
      if (ico) ico.textContent = "↕";
    });
    th.classList.add("sorted");
    const ico = th.querySelector(".sort-icon");
    if (ico) ico.textContent = sortDir === 1 ? "↑" : "↓";

    applyFilters();
  });
});

// ── EVENT LISTENERS ──

// Debounced search: waits 200 ms after the user stops typing before filtering.
// Prevents running the filter on every single keypress.
let debounceTimer;
searchInput.addEventListener("input", () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(applyFilters, 200);
});

// Dropdowns filter immediately on change (no debounce needed)
speedSelect.addEventListener("change", applyFilters);
ratioSelect.addEventListener("change", applyFilters);
brandSelect.addEventListener("change", applyFilters);

// Reset all filters
function resetFilters() {
  searchInput.value = "";
  speedSelect.value = "";
  ratioSelect.value = "";
  brandSelect.value = "";
  sortCol = null;
  sortDir = 1;
  document.querySelectorAll("th[data-col]").forEach((t) => {
    t.classList.remove("sorted");
    const ico = t.querySelector(".sort-icon");
    if (ico) ico.textContent = "↕";
  });
  updateRatioDropdown(); // restore full ratio list
  applyFilters();
}

btnReset.addEventListener("click", resetFilters);
if (btnResetEmpty) btnResetEmpty.addEventListener("click", resetFilters);

// ── SCROLL TO TOP BUTTON ──
// Show the button after scrolling 400px
window.addEventListener("scroll", () => {
  scrollBtn.style.display = window.scrollY > 400 ? "block" : "none";
});

// ── KICK OFF ──
loadAllCassettes();
