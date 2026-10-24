---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.33
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.22
    win_rate: 0.59
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.9
    - name: Leviathan's Hide
      pick_rate: 0.09
      win_rate: 0.71
  - name: Prophetic Cloak
    pick_rate: 0.2
    win_rate: 0.47
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.77
    - name: Leviathan's Hide
      pick_rate: 0.08
      win_rate: 0.67
  - name: Shifter's Shield
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.08
      win_rate: 1.0
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.5
  - name: Soul Reaver
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.43
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.86
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.7
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.71
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.67
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.75
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.54
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.7
  - name: Sundering Axe
    pick_rate: 0.11
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-24'
  god_win_rate: 0.618421052631579
  god_matches_won: 47
  god_matches_played: 76
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Genji''s Guard, Breastplate of Valor, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean
    Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Leviathan''s Hide, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Heartseeker, Rod of Asclepius, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Devourer's Gauntlet
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Asclepius, Golden Blade, Soul Gem, Runeforged Hammer,
    Genji''s Guard, Breastplate of Valor, Shield Splitter, Eye of the Storm, Pharaoh''s
    Curse, The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s
    Lament, Gluttonous Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s
    Grace, Riptalon, Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Helm
    of Radiance, Stone of Binding, Glorious Pridwen, Daybreak Gavel, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.56
    Devourer's Gauntlet:
      total: 0.59
      efficiency: 0.29
      win: 0.9
      pick: 0.13
      fit: 0.48
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.37
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Kinetic Cuirass
  - Devourer's Gauntlet
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Screeching Gargoyle, Gluttonous Grimoire, Genji''s
    Guard, Void Shield, Breastplate of Valor, Spear of Desolation, Spear of the Magus,
    Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian Shard,
    Runeforged Hammer, Silverbranch Bow, Golden Blade, Toxic Blade, Titan''s Bane,
    The Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble
    Ring, Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.47
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Genji''s Guard, Breastplate of
    Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.47
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Amanita Charm, Shield
    of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Shield Splitter, Nimble Ring, Runeforged Hammer, Helm
    of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s Curse, Golden Blade, Eye
    of Providence, Stone of Binding, Draconic Scale, Shogun''s Ofuda, Gladiator''s
    Shield, Eye of the Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the
    Magus, Magi''s Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian
    Shard, Midgardian Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.55
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Runeforged Hammer, Genji''s Guard, Breastplate
    of Valor, Eye of the Storm, Gluttonous Grimoire, Golden Blade, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence,
    Spear of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian
    Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Silverbranch
    Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.52
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.38
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Breastplate
    of Valor, Shield Splitter, Spear of the Magus, Spear of Desolation, Nimble Ring,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Golden Blade, Eye
    of the Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s Harp,
    Heartseeker, Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye of Providence,
    Tyrfing, Shield of the Phoenix, Draconic Scale, Shogun''s Ofuda, Jade Scepter,
    Doom Orb, Silverbranch Bow, Wish-Granting Pearl, Avenging Blade, Death Metal,
    Chronos'' Pendant, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.46
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Shield Splitter, Genji''s Guard, Breastplate of Valor, Golden Blade,
    Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence,
    Lernaean Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.68
      efficiency: 0.56
      win: 0.86
      pick: 0.15
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.3
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
