/** The reasoning behind the six, in words: what the enemy team is doing,
 * what that changed, how the six was chosen, and how the comparison was
 * measured. The desktop second column carries it beside the enemy panel; on
 * a phone it sits behind a "Why this build" disclosure. */
import type { CoreChange } from "../../lib/draftBuild";
import type { ThreatKey } from "../../lib/threats";
import type { SideBySideData } from "../SideBySide";
import type { ComparisonMeta } from "./useComparison";
import { answerWords } from "./itemReason";
import { listWords, MODE_NAME, type Mode } from "./verdict";

const THREAT_WORDS: { key: ThreatKey; label: string }[] = [
  { key: "healers", label: "Healing" },
  { key: "lockdown", label: "Crowd control" },
  { key: "tanks", label: "Tanks" },
  { key: "crit", label: "Crit" },
  { key: "magical", label: "Magical damage" },
  { key: "physical", label: "Physical damage" },
  { key: "walls", label: "Walls" },
];

export function WhyPanel({ god, mode, isModel, buildLabel, changes, culprits, enemiesKnown, comparison, meta, kitLine }: {
  god: string;
  mode: Mode;
  isModel: boolean;
  buildLabel: string;
  changes: CoreChange[];
  culprits: Record<ThreatKey, string[]>;
  enemiesKnown: number;
  comparison: SideBySideData | null;
  meta: ComparisonMeta | null;
  kitLine?: string;
}) {
  const threats = THREAT_WORDS.filter(({ key }) => (culprits[key] ?? []).length > 0);
  return (
    <div data-testid="why-panel" className="space-y-5 text-copy text-muted">
      <section>
        <h3 className="font-cond text-[20px] font-extrabold text-ink">Against this team</h3>
        {enemiesKnown === 0 ? (
          <p className="mt-1">No enemies yet. Add the ones you know and the six re-ranks itself in place.</p>
        ) : (
          <>
            <ul className="mt-1.5 space-y-1">
              {threats.map(({ key, label }) => (
                <li key={key}><span className="text-ink">{label}</span> — {listWords(culprits[key])}</li>
              ))}
            </ul>
            <p className="mt-2">
              {changes.length === 0
                ? `This team doesn't move ${god}'s six — no swap earned enough to displace an item.`
                : changes.map((c) => {
                    const w = answerWords(c.reason);
                    return `${c.added} ${c.removed ? `replaces ${c.removed}` : "comes in"}${w ? ` for ${w}` : ""}.`;
                  }).join(" ")}
            </p>
          </>
        )}
      </section>

      <section>
        <h3 className="font-cond text-[20px] font-extrabold text-ink">How the six is chosen</h3>
        <p className="mt-1">
          {isModel
            ? `Ichor's main six is the model's own answer: each item's stats priced in gold against what it costs, weighed by how well they fit ${god}'s kit — not copied from what's popular.`
            : `The ${buildLabel} build leans the same pricing toward one job. Ichor's main six is the one the comparison measures.`}
          {mode !== "conquest" && ` ${MODE_NAME[mode]} has no win data, so nothing here is ranked on results.`}
        </p>
      </section>

      {mode === "conquest" && comparison && (
        <section>
          <h3 className="font-cond text-[20px] font-extrabold text-ink">How it was measured</h3>
          <p className="mt-1">
            Both sixes play the same fights in a combat model{meta ? ` at level ${meta.level}` : ""}, with item
            passives simulated where the model can. Within ±{Math.round((meta?.band ?? 0.05) * 100)}% is about even.
            {comparison.coverage && ` It simulates ${Math.round(comparison.coverage.ichor * 100)}% of the gold in Ichor's six and ${Math.round(comparison.coverage.community * 100)}% of theirs.`}
          </p>
          {kitLine && <p className="mt-1 text-note text-quiet">{kitLine}</p>}
        </section>
      )}
    </div>
  );
}
