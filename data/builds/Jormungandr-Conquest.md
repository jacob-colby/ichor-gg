---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.42
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.46
    win_rate: 0.62
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.11
      win_rate: 0.69
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.41
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.65
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.14
      win_rate: 0.59
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.67
  - name: Ethereal Staff
    pick_rate: 0.22
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.66
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.48
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.65
  - name: Soul Reaver
    pick_rate: 0.1
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.65
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.56
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.7
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.54
  - name: Gilded Arrow
    pick_rate: 0.08
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-10-30'
  god_win_rate: 0.5991561181434599
  god_matches_won: 142
  god_matches_played: 237
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Genji''s Guard, Shield Splitter, Breastplate of Valor, Golden
    Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of
    Providence, Draconic Scale, Lernaean Bow, Hydra''s Lament, Shield of the Phoenix,
    Shogun''s Ofuda, Stone of Binding, Tyrfing, Helm of Radiance, Nimble Ring, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Midgardian Mail, Mantle Of Discord, Oni
    Hunter''s Garb, Screeching Gargoyle, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel,
    Spear of Desolation, Leviathan''s Hide, Rod of Asclepius, Void Shield, Dominance,
    Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.37
      fit: 0.48
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Shifter's Shield
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
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Jotunn''s Revenge, Kinetic Cuirass, Rod of Asclepius, Golden Blade, Soul Gem,
    Runeforged Hammer, Genji''s Guard, Shield Splitter, Breastplate of Valor, Eye
    of the Storm, Yogi''s Necklace, Pharaoh''s Curse, The Reaper, Erosion, Lernaean
    Bow, Gluttonous Grimoire, Shogun''s Ofuda, Hydra''s Lament, Eye of Providence,
    Phoenix Feather, Chandra''s Grace, Draconic Scale, Tyrfing, Riptalon, Nimble Ring,
    Avenging Blade, Lifebinder, Helm of Radiance, Daybreak Gavel, Midgardian Mail,
    Stone of Binding, Glorious Pridwen, Oni Hunter''s Garb, Bragi''s Harp, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.56
    Ethereal Staff:
      total: 0.59
      efficiency: 0.47
      win: 0.71
      pick: 0.34
      fit: 0.62
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.37
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Ethereal Staff
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Kinetic Cuirass, Gluttonous Grimoire, Screeching
    Gargoyle, Genji''s Guard, Void Shield, Spear of the Magus, Spear of Desolation,
    Breastplate of Valor, Void Stone, Obsidian Shard, Shield Splitter, Soul Gem, Tekko-Kagi,
    Heartseeker, Runeforged Hammer, Silverbranch Bow, Golden Blade, Toxic Blade, Titan''s
    Bane, The Crusher, Hydra''s Lament, Eye of the Storm, Erosion, Lernaean Bow, Pharaoh''s
    Curse, Helm of Radiance, Nimble Ring, The Reaper, Eye of Providence, Shield of
    the Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.5
      win: 0.66
      pick: 0.0
      fit: 0.66
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.66
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Genji''s Guard, Gluttonous Grimoire,
    Breastplate of Valor, Tyrfing, Shield Splitter, Pharaoh''s Curse, Soul Gem, Runeforged
    Hammer, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm
    of Radiance, Eye of Providence, Toxic Blade, Hydra''s Lament, Shield of the Phoenix,
    Eye of the Storm, Stone of Binding, Draconic Scale, Magi''s Cloak, Daybreak Gavel,
    Spear of the Magus, Spear of Desolation, Midgardian Mail, Screeching Gargoyle,
    The Reaper, Bragi''s Harp, Tekko-Kagi, Oni Hunter''s Garb, Rod of Asclepius, Mantle
    Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.52
      win: 0.66
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
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
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Breastplate of Valor, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s Lament, Lotus Sickle,
    Soul Gem, Screeching Gargoyle, Chronos'' Pendant, Shield Splitter, Gladiator''s
    Shield, Helm of Radiance, Nimble Ring, Gluttonous Grimoire, Runeforged Hammer,
    Erosion, Pharaoh''s Curse, Golden Blade, Eye of Providence, Draconic Scale, Stone
    of Binding, Shogun''s Ofuda, Eye of the Storm, Spear of the Magus, Gem of Focus,
    Rod of Asclepius, Lernaean Bow, Arondight, Magi''s Cloak, Daybreak Gavel, Midgardian
    Mail, Obsidian Shard, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.66
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.64
      win: 0.66
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Genji''s Guard,
    Runeforged Hammer, Breastplate of Valor, Eye of the Storm, Gluttonous Grimoire,
    Golden Blade, Hydra''s Lament, Heartseeker, Erosion, Spear of Desolation, Lernaean
    Bow, Spear of the Magus, Eye of Providence, Tekko-Kagi, Avenging Blade, Draconic
    Scale, Shield of the Phoenix, Helm of Radiance, Stone of Binding, Soul Gem, Tyrfing,
    Titan''s Bane, Obsidian Shard, The Crusher, Pharaoh''s Curse, Magi''s Cloak, The
    Reaper, Nimble Ring, Shogun''s Ofuda, Midgardian Mail, Daybreak Gavel, Screeching
    Gargoyle, Oni Hunter''s Garb, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.37
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Genji''s
    Guard, Breastplate of Valor, Spear of the Magus, Spear of Desolation, Shield Splitter,
    Helm of Radiance, Nimble Ring, Runeforged Hammer, Obsidian Shard, Soul Gem, Golden
    Blade, Hydra''s Lament, Eye of the Storm, Rod of Asclepius, Lernaean Bow, Bragi''s
    Harp, Lotus Sickle, Erosion, Pharaoh''s Curse, Tekko-Kagi, Heartseeker, Eye of
    Providence, Shield of the Phoenix, Tyrfing, Jade Scepter, Stone of Binding, Draconic
    Scale, Shogun''s Ofuda, Doom Orb, Silverbranch Bow, Avenging Blade, Death Metal,
    Bracer of The Abyss, Wish-Granting Pearl.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.65
      pick: 0.37
      fit: 0.36
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Genji''s Guard, Shield Splitter, Breastplate of Valor,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse,
    Eye of Providence, Draconic Scale, Lernaean Bow, Hydra''s Lament, Shield of the
    Phoenix, Shogun''s Ofuda, Stone of Binding, Tyrfing, Helm of Radiance, Nimble
    Ring, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Midgardian Mail, Mantle
    Of Discord, Oni Hunter''s Garb, Screeching Gargoyle, Bragi''s Harp, Tekko-Kagi,
    Daybreak Gavel, Spear of Desolation, Leviathan''s Hide, Rod of Asclepius, Void
    Shield, Dominance, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.66
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.66
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.27
      fit: 0.43
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
---
