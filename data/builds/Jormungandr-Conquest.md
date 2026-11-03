---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.43
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.47
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.41
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.61
  - name: Ethereal Staff
    pick_rate: 0.21
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.6
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.52
  - name: Soul Reaver
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.68
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.58
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.48
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.54
  - name: Sundering Axe
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-11-03'
  god_win_rate: 0.5724137931034483
  god_matches_won: 166
  god_matches_played: 290
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Shield Splitter,
    Kinetic Cuirass, Jotunn''s Revenge, Genji''s Guard, Golden Blade, Breastplate
    of Valor, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Oni Hunter''s Garb, Tyrfing, Lernaean Bow, Draconic
    Scale, Shogun''s Ofuda, Stone of Binding, Shield of the Phoenix, Helm of Radiance,
    Helm of Darkness, Midgardian Mail, Magi''s Cloak, Eros'' Bow, Titan''s Bane, Gluttonous
    Grimoire, Nimble Ring, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Dominance,
    Arondight, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Shield of the Phoenix,
    Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Soul Gem,
    Golden Blade, Runeforged Hammer, Phoenix Feather, Yogi''s Necklace, The Reaper,
    Breastplate of Valor, Tekko-Kagi, Hydra''s Lament, Pharaoh''s Curse, Oni Hunter''s
    Garb, Tyrfing, Chandra''s Grace, Lernaean Bow, Erosion, Eye of Providence, Shogun''s
    Ofuda, Eros'' Bow, Gluttonous Grimoire, Draconic Scale, Avenging Blade, Blood-Bound
    Book, Midgardian Mail, Regrowth Striders, Rod of Asclepius, Titan''s Bane, Nimble
    Ring, Helm of Radiance, Leviathan''s Hide, Sphere of Negation, Spear of Desolation,
    Glorious Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.56
    Ethereal Staff:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.33
      fit: 0.62
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.32
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Ethereal Staff
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Tekko-Kagi, Genji''s Guard, Screeching Gargoyle, Avenging Blade,
    Shield Splitter, Kinetic Cuirass, Titan''s Bane, Gluttonous Grimoire, Obsidian
    Shard, Spear of Desolation, Void Stone, Void Shield, Soul Gem, Breastplate of
    Valor, Runeforged Hammer, The Crusher, Toxic Blade, Spear of the Magus, Silverbranch
    Bow, Golden Blade, Heartseeker, Hydra''s Lament, The Reaper, Oni Hunter''s Garb,
    Helm of Radiance, Lernaean Bow, Erosion, Tyrfing, Pharaoh''s Curse, Eye of Providence,
    Doom Orb, Nimble Ring, Draconic Scale, Midgardian Mail, The World Stone, Shield
    of the Phoenix.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.24
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble
    Ring, Kinetic Cuirass, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s Lament,
    Shogun''s Ofuda, Silverbranch Bow, Eros'' Bow, Helm of Radiance, Erosion, Eye
    of Providence, Stone of Binding, Draconic Scale, Obsidian Shard, Midgardian Mail,
    Shield of the Phoenix, Spear of Desolation, Helm of Darkness, The Reaper, Magi''s
    Cloak, Screeching Gargoyle, Titan''s Bane, Riptalon, Leviathan''s Hide, Dominance,
    Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Genji''s Guard, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Kinetic
    Cuirass, Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, Shield Splitter,
    Soul Gem, Screeching Gargoyle, Lotus Sickle, Chronos'' Pendant, Helm of Radiance,
    Arondight, Runeforged Hammer, Oni Hunter''s Garb, Gluttonous Grimoire, Nimble
    Ring, Golden Blade, Helm of Darkness, Erosion, Obsidian Shard, Pharaoh''s Curse,
    Eye of Providence, Eros'' Bow, Gladiator''s Shield, Stone of Binding, Tekko-Kagi,
    Draconic Scale, Midgardian Mail, Gem of Focus, Shogun''s Ofuda, Magi''s Cloak,
    Heartwood Charm, Lernaean Bow, Tyrfing, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.27
      fit: 0.55
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Genji''s Guard, Kinetic Cuirass, Runeforged
    Hammer, Tekko-Kagi, Titan''s Bane, Hydra''s Lament, Breastplate of Valor, Golden
    Blade, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, The Crusher,
    Oni Hunter''s Garb, Erosion, Tyrfing, Lernaean Bow, Eye of Providence, Avenging
    Blade, Soul Gem, Heartseeker, Helm of Radiance, Draconic Scale, Stone of Binding,
    The Reaper, Shield of the Phoenix, Arondight, Midgardian Mail, Helm of Darkness,
    Magi''s Cloak, Pharaoh''s Curse, Death Metal, Spear of the Magus, Screeching Gargoyle,
    Wyrmskin Hide, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.27
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Shield Splitter, Kinetic Cuirass,
    Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Soul Gem,
    Helm of Radiance, Runeforged Hammer, Breastplate of Valor, Nimble Ring, Titan''s
    Bane, Golden Blade, Helm of Darkness, Spear of the Magus, Hydra''s Lament, Eros''
    Bow, Bragi''s Harp, Death Metal, Oni Hunter''s Garb, Lernaean Bow, Tyrfing, Ancient
    Signet, Lotus Sickle, Erosion, Pharaoh''s Curse, Eye of Providence, The Crusher,
    Jade Scepter, Stone of Binding, Doom Orb, Midgardian Mail, Draconic Scale, Shield
    of the Phoenix, Toxic Blade, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.35
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.41
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.23
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Shield
    Splitter, Kinetic Cuirass, Jotunn''s Revenge, Genji''s Guard, Golden Blade, Breastplate
    of Valor, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Oni Hunter''s Garb, Tyrfing, Lernaean Bow, Draconic
    Scale, Shogun''s Ofuda, Stone of Binding, Shield of the Phoenix, Helm of Radiance,
    Helm of Darkness, Midgardian Mail, Magi''s Cloak, Eros'' Bow, Titan''s Bane, Gluttonous
    Grimoire, Nimble Ring, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Leviathan''s Hide, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Dominance,
    Arondight, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.61
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  starter: *id001
---
