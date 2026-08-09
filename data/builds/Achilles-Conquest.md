---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.51
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.51
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.19
      win_rate: 0.51
    - name: Runeforged Hammer
      pick_rate: 0.12
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.11
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.24
      win_rate: 0.53
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.58
  - name: Gladiator's Shield
    pick_rate: 0.07
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.46
  - name: Dwarven Plate
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.46
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.6
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.54
    - name: Glorious Pridwen
      pick_rate: 0.05
      win_rate: 0.62
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.57
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.48
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.56
  community_starters:
  - name: Sundering Axe
    pick_rate: 0.24
    win_rate: 0.56
  - name: Warrior's Axe
    pick_rate: 0.21
    win_rate: 0.46
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-08-09'
  god_win_rate: 0.5065243179122183
  god_matches_won: 427
  god_matches_played: 843
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-09'
  god_matches_analyzed: 15881
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, The Crusher, Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Kinetic Cuirass, Eye of Providence, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of the Storm, Avenging Blade, Shield Splitter, Golden Blade, The Reaper, Spectral
    Armor, Shield of the Phoenix, Yogi''s Necklace, Breastplate of Valor, Lernaean
    Bow, Erosion, Pharaoh''s Curse, Damaru, Genji''s Guard, Freya''s Tears, Heartseeker,
    Draconic Scale, Leviathan''s Hide, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, The Crusher, Eye of Providence, Jotunn''s Revenge, The Reaper,
    Oni Hunter''s Garb, Eye of the Storm, Shield Splitter, Hydra''s Lament, Chandra''s
    Grace, Erosion, Riptalon, Phoenix Feather, Spectral Armor, Avenging Blade, Freya''s
    Tears, Golden Blade, Breastplate of Valor, Draconic Scale, Pharaoh''s Curse, Yogi''s
    Necklace, Genji''s Guard, Leviathan''s Hide, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Runeforged Hammer, Avenging Blade,
    Berserker''s Shield, Amanita Charm, The Reaper, Kinetic Cuirass, Eye of Providence,
    Heartseeker, Oni Hunter''s Garb, Hydra''s Lament, Void Shield, Stone of Binding,
    Eye of the Storm, Riptalon, Titan''s Bane, Tekko-Kagi, Void Stone, Screeching
    Gargoyle, Golden Blade, Yogi''s Necklace, Shield Splitter, Breastplate of Valor,
    Silverbranch Bow, Spectral Armor, Genji''s Guard, Pendulum Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.78
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.48
    The Crusher:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Riptalon
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Runeforged Hammer, Golden Blade, Riptalon, The
    Crusher, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Pharaoh''s Curse,
    Silverbranch Bow, Lernaean Bow, Oni Hunter''s Garb, Eye of Providence, Tyrfing,
    Hydra''s Lament, Shogun''s Ofuda, Breastplate of Valor, Yogi''s Necklace, Toxic
    Blade, Genji''s Guard, Dominance, Spectral Armor, The Reaper, Shield of the Phoenix,
    Freya''s Tears, Avenging Blade, Tekko-Kagi, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.62
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.34
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - Runeforged Hammer
  flex_slots:
  - Runeforged Hammer
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Breastplate of Valor, Genji''s Guard, Runeforged Hammer, Shield of the Phoenix,
    Freya''s Tears, Berserker''s Shield, Amanita Charm, The Crusher, Kinetic Cuirass,
    Eye of Providence, Oni Hunter''s Garb, Chandra''s Grace, Screeching Gargoyle,
    Yogi''s Necklace, Gladiator''s Shield, Arondight, Spectral Armor, Pharaoh''s Curse,
    Pendulum Blade, Eye of the Storm, Avenging Blade, Golden Blade, Erosion, Shield
    Splitter, Leviathan''s Hide, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.43
      pick: 0.11
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Runeforged
    Hammer, Berserker''s Shield, Kinetic Cuirass, Eye of Providence, Oni Hunter''s
    Garb, Hydra''s Lament, Genji''s Guard, Eye of the Storm, Avenging Blade, Shield
    Splitter, Golden Blade, The Reaper, Spectral Armor, Shield of the Phoenix, Yogi''s
    Necklace, Breastplate of Valor, Lernaean Bow, Erosion, Pharaoh''s Curse, Damaru,
    Freya''s Tears, Heartseeker, Draconic Scale, Leviathan''s Hide, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.55
      pick: 0.12
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
