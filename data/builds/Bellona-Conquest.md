---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.54
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.55
    alternates:
    - name: Golden Blade
      pick_rate: 0.21
      win_rate: 0.62
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.55
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.47
    alternates:
    - name: Golden Blade
      pick_rate: 0.15
      win_rate: 0.56
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.46
  - name: Shogun's Ofuda
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.28
      win_rate: 0.63
    - name: Kinetic Cuirass
      pick_rate: 0.14
      win_rate: 0.56
  - name: Kinetic Cuirass
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.14
      win_rate: 0.48
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.51
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.74
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.57
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.06
    win_rate: 0.46
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.64
    - name: Hastened Fatalis
      pick_rate: 0.04
      win_rate: 0.8
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.46
    win_rate: 0.58
  - name: Death's Toll
    pick_rate: 0.33
    win_rate: 0.47
  - name: Bumba's Golden Dagger
    pick_rate: 0.09
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-08'
  god_win_rate: 0.5388235294117647
  god_matches_won: 229
  god_matches_played: 425
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Genji''s Guard, Jotunn''s
    Revenge, Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Hide of the Nemean Lion, Hydra''s Lament, Breastplate of Valor, Eye
    of the Storm, Shield of the Phoenix, Erosion, Draconic Scale, Spectral Armor,
    Pharaoh''s Curse, Avenging Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Stone of Binding, Lernaean Bow.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.41
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.31
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.7
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.4
      fit: 0.6
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shield of the Phoenix, Eye of Providence,
    Runeforged Hammer, Genji''s Guard, Jotunn''s Revenge, Oni Hunter''s Garb, The
    Crusher, Hydra''s Lament, Chandra''s Grace, Eye of the Storm, Shield Splitter,
    The Reaper, Freya''s Tears, Breastplate of Valor, Erosion, Phoenix Feather, Spectral
    Armor, Avenging Blade, Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Leviathan''s
    Hide, Midgardian Mail, Riptalon.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.47
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.31
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.68
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.4
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Jotunn''s Revenge, The Crusher, Amanita Charm,
    Genji''s Guard, Avenging Blade, Eye of Providence, Stone of Binding, Oni Hunter''s
    Garb, Runeforged Hammer, Screeching Gargoyle, Hydra''s Lament, Breastplate of
    Valor, Freya''s Tears, Void Shield, Shield Splitter, The Reaper, Void Stone, Shield
    of the Phoenix, Eye of the Storm, Spectral Armor, Heartseeker, Erosion, Yogi''s
    Necklace, Pharaoh''s Curse, Draconic Scale, Riptalon.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.53
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.4
      fit: 0.43
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Hastened Fatalis
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shogun''s Ofuda, Genji''s Guard, Eye
    of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher, Jotunn''s Revenge,
    Riptalon, Breastplate of Valor, Runeforged Hammer, Freya''s Tears, Lernaean Bow,
    Hydra''s Lament, Tyrfing, Shield of the Phoenix, Silverbranch Bow, Spectral Armor,
    Shield Splitter, Yogi''s Necklace, Erosion, Eye of the Storm, Draconic Scale,
    Dominance, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.47
      pick: 0.31
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.48
    Hastened Fatalis:
      total: 0.53
      efficiency: 0.32
      win: 0.8
      pick: 0.04
      fit: 0.34
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.4
      fit: 0.38
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Dwarven Plate — magical protection
    swap_item: Dwarven Plate
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Freya''s
    Tears, Breastplate of Valor, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix,
    Hydra''s Lament, Eye of Providence, Oni Hunter''s Garb, The Crusher, Runeforged
    Hammer, Screeching Gargoyle, Chandra''s Grace, Gladiator''s Shield, Spectral Armor,
    Erosion, Shield Splitter, Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak,
    Draconic Scale, Eye of the Storm, Arondight, Leviathan''s Hide, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.4
      fit: 0.45
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Genji''s
    Guard, Jotunn''s Revenge, Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb,
    Freya''s Tears, The Crusher, Hydra''s Lament, Breastplate of Valor, Eye of the
    Storm, Shield of the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s
    Curse, Avenging Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Lernaean Bow, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.31
      fit: 0.38
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Dwarven Plate
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Dwarven Plate
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye
    of Providence, Genji''s Guard, Jotunn''s Revenge, Shield Splitter, Runeforged
    Hammer, Oni Hunter''s Garb, Freya''s Tears, The Crusher, Hydra''s Lament, Breastplate
    of Valor, Eye of the Storm, Shield of the Phoenix, Erosion, Draconic Scale, Spectral
    Armor, Pharaoh''s Curse, Avenging Blade, Yogi''s Necklace, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Stone of Binding, Lernaean Bow, Hide of the
    Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.31
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.6
      pick: 0.13
      fit: 0.7
    Dwarven Plate:
      total: 0.53
      efficiency: 0.35
      win: 0.74
      pick: 0.12
      fit: 0.43
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  swaps:
  - added: Dwarven Plate
    removed: Jotunn's Revenge
    reason: community 74% win over 51 matches (vs 54% on this god), taking the model's
      weakest slot from Jotunn's Revenge
  starter: *id001
---
