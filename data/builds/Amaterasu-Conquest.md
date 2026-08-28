---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.34
    win_rate: 0.65
    alternates:
    - name: Golden Blade
      pick_rate: 0.32
      win_rate: 0.65
    - name: Bragi's Harp
      pick_rate: 0.09
      win_rate: 0.55
  - name: Golden Blade
    pick_rate: 0.25
    win_rate: 0.66
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.22
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.15
      win_rate: 0.61
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.62
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.58
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.71
  - name: Draconic Scale
    pick_rate: 0.15
    win_rate: 0.73
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.05
      win_rate: 0.8
  - name: Veve Charm
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.75
  - name: Death's Embrace
    pick_rate: 0.19
    win_rate: 0.41
  - name: Death's Toll
    pick_rate: 0.18
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-08-28'
  god_win_rate: 0.6068376068376068
  god_matches_won: 71
  god_matches_played: 117
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-28'
  god_matches_analyzed: 3498
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield Splitter, Genji''s
    Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion, Eye
    of Providence, Shield of the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord,
    Screeching Gargoyle, Midgardian Mail, Hide of the Nemean Lion, Spear of Desolation,
    Leviathan''s Hide, Void Shield, Stampede, Ancile, Heartseeker, Oni Hunter''s Garb,
    Daybreak Gavel, Rod of Asclepius, Soul Gem, Void Stone, Xibalban Effigy, Spectral
    Armor, Helm of Darkness, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.67
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.53
    Shifter's Shield:
      total: 0.59
      efficiency: 0.55
      win: 0.65
      pick: 0.34
      fit: 0.57
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.57
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Rod of Asclepius, Runeforged Hammer, Soul Gem, Shield Splitter, Genji''s Guard,
    Breastplate of Valor, Eye of the Storm, Ethereal Staff, Erosion, Eye of Providence,
    The Reaper, Yogi''s Necklace, Hydra''s Lament, Phoenix Feather, Gluttonous Grimoire,
    Chandra''s Grace, Avenging Blade, Glorious Pridwen, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Daybreak Gavel, Hide of the Nemean Lion, Screeching
    Gargoyle, Sphere of Negation, Magi''s Cloak, Leviathan''s Hide, Spear of Desolation,
    Void Shield, Stampede, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.65
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.46
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.65
      pick: 0.34
      fit: 0.55
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.55
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Avenging Blade, Genji''s Guard, Spear
    of Desolation, Void Shield, Breastplate of Valor, Spear of the Magus, Heartseeker,
    Soul Gem, Shield Splitter, Void Stone, Obsidian Shard, Runeforged Hammer, Titan''s
    Bane, The Crusher, Eye of the Storm, Erosion, Hydra''s Lament, The Reaper, Eye
    of Providence, Shield of the Phoenix, Helm of Radiance, Doom Orb, The World Stone,
    Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Mantle Of Discord, Avatar''s Parashu,
    Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.39
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.34
      fit: 0.42
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Draconic Scale
  - Shogun's Ofuda
  flex_slots:
  - Freya's Tears
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Nimble
    Ring, Genji''s Guard, Gluttonous Grimoire, Breastplate of Valor, Tyrfing, Shield
    Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Silverbranch Bow, Erosion, Helm of Radiance, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Eye of Providence, Eye of the Storm, Toxic Blade, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of Desolation, The Reaper, Spear of
    the Magus, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade, Bragi''s Harp.'
  slot_scores:
    Golden Blade:
      total: 0.58
      efficiency: 0.52
      win: 0.66
      pick: 0.34
      fit: 0.53
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.46
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.34
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.36
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.11
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Shield Splitter, Erosion, Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Stone of Binding, Eye of the Storm, Arondight,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide, Jade Scepter,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.64
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Spear of Desolation, Genji''s Guard, Breastplate of
    Valor, Soul Gem, Spear of the Magus, Helm of Radiance, Obsidian Shard, Shield
    Splitter, Runeforged Hammer, Rod of Asclepius, Hydra''s Lament, Shield of the
    Phoenix, Chronos'' Pendant, Eye of the Storm, Erosion, Jade Scepter, Doom Orb,
    Heartseeker, Eye of Providence, Wish-Granting Pearl, Stone of Binding, The World
    Stone, Ancient Signet, Death Metal, Helm of Darkness, Screeching Gargoyle, Dreamer''s
    Idol, Magi''s Cloak, Avenging Blade, Ethereal Staff, Triton''s Conch, Daybreak
    Gavel, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.49
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.39
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.34
      fit: 0.39
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.39
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Breastplate of Valor, Spear
    of Desolation, Shield Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer,
    Helm of Radiance, Obsidian Shard, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade, Chronos''
    Pendant, Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, Screeching
    Gargoyle, Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.51
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.38
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.34
      fit: 0.41
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.32
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the
    Storm, Erosion, Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Stone
    of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Hide of the Nemean Lion,
    Spear of Desolation, Leviathan''s Hide, Void Shield, Stampede, Ancile, Heartseeker,
    Oni Hunter''s Garb, Daybreak Gavel, Rod of Asclepius, Soul Gem, Void Stone, Xibalban
    Effigy, Spectral Armor, Helm of Darkness, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.75
      pick: 0.18
      fit: 0.67
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.62
      pick: 0.4
      fit: 0.53
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.57
  starter: *id001
---
