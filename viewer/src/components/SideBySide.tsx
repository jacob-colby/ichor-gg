/** Done criterion 2 on the god page: Ichor's build beside the community's,
 * both run through the combat model with item passives SIMULATED.
 *
 * The numbers are the pipeline's (`python -m smite.side_by_side --json`); this
 * only draws them. One small file per god, fetched when the section mounts, so
 * the index does not carry ~1 MB nobody opened.
 *
 * Principle 3 is the shape of the section: a passive the model cannot simulate
 * is NAMED, with its reason, beside the build it sits in — "not simulated" and
 * "worth nothing" must never render the same way. */
import { useEffect, useState } from "react";
import { iconSlug } from "../lib/builds";
import { ItemIcon } from "./ItemIcon";

type Metric = "sustained_squishy" | "sustained_tank" | "burst_squishy" | "burst_tank"
  | "ehp_physical" | "ehp_magical";

interface PassiveNote { item?: string; status: string; summary: string; assumptions: string[];
  worth?: Record<Metric, number> }

interface Side extends Record<Metric, number> {
  items: string[]; gold: number;
  mean_cooldown: number | null; ultimate_cooldown: number | null;
  crit_chance: number; crit_multiplier: number; crit_ev: number;
  passives: (PassiveNote & { item: string })[];
  breakpoints: Record<string, Record<Metric, number>>;
}

interface Diff {
  item: string; side: "community" | "ichor"; gold: number;
  community: { pick_rate: number; win_rate: number | null; where: string };
  passive: PassiveNote;
  model: { text: string };
  best_swap?: { replaces: string; damage_axis: number; survival_axis: number };
}

export interface SideBySideData {
  god: string; verdict: string; damage_axis: number; survival_axis: number;
  shared: string[]; ichor: Side; community: Side; diffs: Diff[];
  substitutions: { dropped: string; used: string | null; note?: string }[];
  /** Which kit the comparison is on. Absent in files written before
   *  2026-11-02's aspect matching; read as the base kit. */
  kit?: Kit;
}

interface Kit { kit: string; aspect: string | null; pick_rate: number | null;
  win_rate: number | null; simulated: boolean }

const ASPECT_NOT_SIMULATED = "aspect not simulated";

/** The kit line every comparison carries: which kit, and how often the
 *  community plays the aspect. */
function KitLine({ kit }: { kit?: Kit }) {
  const played = kit?.aspect && kit.pick_rate != null
    ? `${kit.aspect} in ${Math.round(kit.pick_rate * 100)}% of games` : null;
  const text = !kit || kit.kit === "base"
    ? `Base kit${played ? ` — the community plays ${played}` : ""}`
    : `${kit.aspect} — the community plays it in ${Math.round((kit.pick_rate ?? 0) * 100)}% of games`;
  return <p className="mt-1 font-mono text-label text-faint" data-testid="kit">Kit: {text}</p>;
}

interface Meta { data: string; level: number; window: number; band: number;
  targets: Record<"squishy" | "tank", { role: string; n: number; max_health: number;
    physical_prot: number; magical_prot: number }> }

type Load<T> = { state: "loading" } | { state: "none" } | { state: "ready"; value: T };

function useJson<T>(url: string): Load<T> {
  const [out, setOut] = useState<Load<T>>({ state: "loading" });
  useEffect(() => {
    let live = true;
    setOut({ state: "loading" });
    fetch(url, { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : null))
      .then((v) => live && setOut(v ? { state: "ready", value: v as T } : { state: "none" }))
      .catch(() => live && setOut({ state: "none" }));
    return () => { live = false; };
  }, [url]);
  return out;
}

const pct = (r: number) => `${r >= 1 ? "+" : "−"}${Math.abs((r - 1) * 100).toFixed(1)}%`;
const n0 = (v: number) => Math.round(v).toLocaleString("en-US");
const secs = (v: number | null) => (v == null ? "—" : `${v.toFixed(1)}s`);
const signed = (v: number) => `${v >= 0 ? "+" : "−"}${n0(Math.abs(v))}`;

/** Tone of a ratio from Ichor's side, inside the verdict band = neutral. */
function tone(r: number, band: number) {
  if (r > 1 + band) return "text-under";
  if (r < 1 - band) return "text-premium";
  return "text-muted";
}

const VERDICT_TONE: Record<string, string> = {
  "Ichor better": "border-under/50 text-under",
  "community better": "border-premium/50 text-premium",
  "trade-off": "border-line-strong text-ink-soft",
  "level": "border-line-strong text-muted",
  [ASPECT_NOT_SIMULATED]: "border-dashed border-line-strong text-muted",
};

const ROWS: { key: Metric; label: string }[] = [
  { key: "burst_squishy", label: "Burst combo · squishy" },
  { key: "burst_tank", label: "Burst combo · tank" },
  { key: "sustained_squishy", label: "10s sustained · squishy" },
  { key: "sustained_tank", label: "10s sustained · tank" },
  { key: "ehp_physical", label: "Effective health · physical" },
  { key: "ehp_magical", label: "Effective health · magical" },
];

const head = "font-mono text-label uppercase tracking-[0.1em] text-faint";

function BuildColumn({ label, side, shared, accent }: {
  label: string; side: Side; shared: Set<string>; accent: boolean }) {
  return (
    <div className="min-w-0">
      <div className="flex items-baseline justify-between gap-2">
        <h3 className={`font-display text-body font-semibold ${accent ? "text-gold" : "text-ink"}`}>{label}</h3>
        <span className="font-mono text-label text-faint">{n0(side.gold)}g</span>
      </div>
      <ol className="mt-2 flex flex-col gap-1">
        {side.items.map((name, i) => {
          const same = shared.has(name);
          return (
            <li key={name} className={`flex items-center gap-2 rounded-md px-1.5 py-1 ${same ? "opacity-60" : "bg-bg2"}`}>
              <span className="w-3 flex-none text-right font-mono text-micro text-faint">{i + 1}</span>
              <ItemIcon name={name} className="h-6 w-6" />
              <span className="truncate text-small text-ink-soft">{name}</span>
              {same && <span className="ml-auto flex-none text-micro text-faint">both</span>}
            </li>
          );
        })}
      </ol>
    </div>
  );
}

function MetricTable({ d, band }: { d: SideBySideData; band: number }) {
  const { ichor: a, community: b } = d;
  const row = (label: string, x: string, y: string, delta?: string, cls = "text-muted") => (
    <tr key={label} className="border-t border-line">
      <th scope="row" className="py-1.5 pr-2 text-left text-small font-normal text-muted">{label}</th>
      <td className="py-1.5 pl-2 text-right font-mono text-small tabular-nums text-ink">{x}</td>
      <td className="py-1.5 pl-2 text-right font-mono text-small tabular-nums text-ink-soft">{y}</td>
      <td className={`py-1.5 pl-2 text-right font-mono text-small tabular-nums ${cls}`}>{delta ?? ""}</td>
    </tr>
  );
  return (
    <table className="mt-4 w-full max-w-[40rem] border-collapse">
      <caption className="sr-only">Ichor against the community, passives simulated</caption>
      <thead>
        <tr>
          <th scope="col" className={`pb-1 text-left ${head}`}>Level 20</th>
          <th scope="col" className={`pb-1 text-right ${head}`}>Ichor</th>
          <th scope="col" className={`pb-1 text-right ${head}`}>Comm.</th>
          <th scope="col" className={`pb-1 text-right ${head}`}>Δ</th>
        </tr>
      </thead>
      <tbody>
        {ROWS.map(({ key, label }) => {
          const r = b[key] ? a[key] / b[key] : 1;
          return row(label, n0(a[key]), n0(b[key]), pct(r), tone(r, band));
        })}
        {row("Mean ability cooldown", secs(a.mean_cooldown), secs(b.mean_cooldown))}
        {row("Ultimate cooldown", secs(a.ultimate_cooldown), secs(b.ultimate_cooldown))}
        {row("Crit expected value", `×${a.crit_ev.toFixed(2)}`, `×${b.crit_ev.toFixed(2)}`)}
        {["2", "4", "6"].map((k) => {
          const x = a.breakpoints[k]?.sustained_squishy ?? 0;
          const y = b.breakpoints[k]?.sustained_squishy ?? 0;
          const r = y ? x / y : 1;
          return row(`${k} items · 10s vs squishy`, n0(x), n0(y), pct(r), tone(r, band));
        })}
      </tbody>
    </table>
  );
}

function DiffItem({ d }: { d: Diff }) {
  const c = d.community;
  const w = d.passive.worth;
  const rates = c.win_rate == null
    ? "not in this god's community record"
    : `${Math.round(c.pick_rate * 100)}% pick · ${Math.round(c.win_rate * 100)}% win · ${c.where}`;
  const notSim = d.passive.status === "not simulated";
  return (
    <li className="rounded-md border border-line bg-bg1 p-3">
      <div className="flex items-start gap-2.5">
        <ItemIcon name={d.item} className="h-8 w-8" />
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-baseline gap-x-2">
            <span className="font-medium text-ink">{d.item}</span>
            <span className={`text-micro uppercase tracking-[0.06em] ${d.side === "ichor" ? "text-gold" : "text-ink-soft"}`}>
              {d.side === "ichor" ? "Ichor only" : "Community only"}
            </span>
            <span className="font-mono text-micro text-faint">{n0(d.gold)}g</span>
          </div>
          <p className="mt-0.5 font-mono text-label text-faint">{rates}</p>
        </div>
      </div>
      <dl className="mt-2 grid gap-1.5 text-small leading-relaxed">
        <div>
          <dt className="inline text-faint">Passive </dt>
          <dd className="inline text-ink-soft">
            {d.passive.summary || "none"}
            {notSim && <span className="ml-1 text-muted">— not simulated{d.passive.assumptions[0] ? `: ${d.passive.assumptions[0]}` : ""}</span>}
            {w && (
              <span className="mt-0.5 block font-mono text-label text-muted">
                worth {signed(w.sustained_squishy)} dmg in 10s · {signed(w.burst_squishy)} burst
                {(w.ehp_physical || w.ehp_magical) ? ` · ${signed(w.ehp_physical)} EHP phys` : ""}
                {d.passive.status === "partial" ? " · partly simulated" : ""}
              </span>
            )}
          </dd>
        </div>
        <div>
          <dt className="inline text-faint">Model </dt>
          <dd className="inline text-muted">{d.model.text.replace(/^model /, "")}</dd>
        </div>
        {d.best_swap && (
          <div>
            <dt className="inline text-faint">In Ichor&rsquo;s build </dt>
            <dd className="inline text-muted">
              for {d.best_swap.replaces}: damage{" "}
              <span className="font-mono text-ink-soft">{pct(d.best_swap.damage_axis)}</span>, survival{" "}
              <span className="font-mono text-ink-soft">{pct(d.best_swap.survival_axis)}</span>
            </dd>
          </div>
        )}
      </dl>
    </li>
  );
}

export function SideBySideView({ d, meta }: { d: SideBySideData; meta: Meta | null }) {
  const band = meta?.band ?? 0.05;
  const shared = new Set(d.shared);
  const gaps = new Map<string, string>();
  for (const p of [...d.ichor.passives, ...d.community.passives]) {
    if (p.status === "not simulated" || p.status === "partial") {
      gaps.set(p.item, `${p.status}: ${p.assumptions.join("; ") || p.summary}`);
    }
  }
  return (
    <section className="mt-7 border-t border-line pt-5" data-testid="side-by-side">
      <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-2">
        <h2 className="font-display text-title font-semibold text-ink">Ichor vs the community</h2>
        <span className={`rounded-full border px-2.5 py-0.5 text-small font-semibold ${VERDICT_TONE[d.verdict] ?? "border-line text-muted"}`}
          data-testid="verdict">
          {d.verdict === "Ichor better" ? "Ichor better" : d.verdict === "community better" ? "Community better"
            : d.verdict === "trade-off" ? "A real trade-off"
            : d.verdict === ASPECT_NOT_SIMULATED ? "No verdict" : "Level"}
        </span>
      </div>
      <KitLine kit={d.kit} />
      {d.verdict === ASPECT_NOT_SIMULATED ? (
        <p className="mt-2 max-w-[70ch] rounded-md border border-dashed border-line-strong bg-bg1 p-3 text-small leading-relaxed text-ink-soft"
          data-testid="aspect-not-simulated">
          Most of this god&rsquo;s players run {d.kit?.aspect}, and the combat model can&rsquo;t
          play an aspect&rsquo;s kit yet. The community build was made for that kit, so the
          numbers below — on the base kit — are not a fair comparison and carry no verdict.
        </p>
      ) : (
        <p className="mt-1.5 max-w-[70ch] text-small leading-relaxed text-muted">
          Both builds run through the combat model with item passives simulated, not priced.
          Ichor&rsquo;s damage is{" "}
          <span className={`font-mono ${tone(d.damage_axis, band)}`}>{pct(d.damage_axis)}</span> and its
          survival{" "}
          <span className={`font-mono ${tone(d.survival_axis, band)}`}>{pct(d.survival_axis)}</span> against
          the community&rsquo;s; within ±{Math.round(band * 100)}% counts as level.
        </p>
      )}

      <div className="mt-4 grid gap-4 sm:grid-cols-2">
        <BuildColumn label="Ichor" side={d.ichor} shared={shared} accent />
        <BuildColumn label="Community" side={d.community} shared={shared} accent={false} />
      </div>
      {d.substitutions.some((s) => s.used) && (
        <p className="mt-2 text-label text-faint">
          Community six cleaned:{" "}
          {d.substitutions.filter((s) => s.used).map((s) => `${s.dropped} → ${s.used}`).join(", ")}
          {" "}(components and statless relics replaced from the community&rsquo;s own record).
        </p>
      )}

      <MetricTable d={d} band={band} />

      {d.diffs.length > 0 && (
        <>
          <h3 className="mt-6 font-display text-body font-semibold text-ink">Where the builds differ, and why</h3>
          <ul className="mt-2 grid gap-2 lg:grid-cols-2">
            {d.diffs.map((x) => <DiffItem key={`${x.side}-${x.item}`} d={x} />)}
          </ul>
        </>
      )}

      {gaps.size > 0 && (
        <details className="mt-4 rounded-md border border-line bg-bg1 p-3 text-small" data-testid="not-simulated">
          <summary className="cursor-pointer text-ink-soft">
            Not simulated in these builds ({gaps.size}) — their value is missing from the numbers above
          </summary>
          <ul className="mt-2 grid gap-1 text-muted">
            {[...gaps].map(([item, why]) => (
              <li key={item}><span className="text-ink-soft">{item}</span> — {why}</li>
            ))}
          </ul>
        </details>
      )}

      {meta && (
        <p className="mt-3 max-w-[74ch] text-label leading-relaxed text-faint">
          Level {meta.level}, one target in range for {meta.window}s, no cast times, no crowd control.
          Squishy = median {meta.targets.squishy.role} in its community build
          ({n0(meta.targets.squishy.max_health)} HP, {n0(meta.targets.squishy.physical_prot)}/{n0(meta.targets.squishy.magical_prot)} prot);
          tank = median {meta.targets.tank.role}
          ({n0(meta.targets.tank.max_health)} HP, {n0(meta.targets.tank.physical_prot)}/{n0(meta.targets.tank.magical_prot)} prot).
          Stacking items count full stacks at six items and none at two and four. Data: {meta.data}.
        </p>
      )}
    </section>
  );
}

/** The section as the god page mounts it. Renders nothing when this god has
 *  no comparison (an empty heading would claim a measurement that is not there). */
export function SideBySide({ god }: { god: string }) {
  const one = useJson<SideBySideData>(`/side_by_side/${iconSlug(god)}.json`);
  const meta = useJson<Meta>("/side_by_side/_meta.json");
  if (one.state === "loading") {
    return <div className="mt-7 h-24 animate-pulse rounded-md bg-bg1" aria-busy="true" aria-label="Loading comparison" />;
  }
  if (one.state === "none") return null;
  return <SideBySideView d={one.value} meta={meta.state === "ready" ? meta.value : null} />;
}
