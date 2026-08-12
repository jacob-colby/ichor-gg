---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.5
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.71
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.66
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.66
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.56
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.66
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.52
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.58
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.21
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.45
  - name: Sundering Axe
    pick_rate: 0.14
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-11'
  god_win_rate: 0.5458996328029376
  god_matches_won: 446
  god_matches_played: 817
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Draconic Scale, Stampede, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Berserker''s Shield, Breastplate of Valor, Oni Hunter''s Garb,
    Gluttonous Grimoire, Hide of the Nemean Lion, Shield of the Phoenix, Erosion,
    Spectral Armor, Shield Splitter, Pharaoh''s Curse, Jotunn''s Revenge, Runeforged
    Hammer, The Crusher, Leviathan''s Hide, Soul Gem, Eye of the Storm, Hydra''s Lament,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Yogi''s Necklace, Shogun''s
    Ofuda, Helm of Radiance, Magi''s Cloak, Ancile, Rod of Asclepius, Gladiator''s
    Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s Wings, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.62
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.68
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
    Stampede:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.44
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Draconic Scale, Stampede, Shield of the
    Phoenix, Kinetic Cuirass, Eye of Providence, Berserker''s Shield, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Breastplate of Valor, Oni Hunter''s Garb, Hide of
    the Nemean Lion, Chandra''s Grace, Erosion, Phoenix Feather, Spectral Armor, Runeforged
    Hammer, Pharaoh''s Curse, Jotunn''s Revenge, Lifebinder, Yogi''s Necklace, Leviathan''s
    Hide, Eye of the Storm, The Crusher, Blood-Bound Book, Midgardian Mail, Shield
    Splitter, Bancroft''s Talon, Hydra''s Lament, Glorious Pridwen, Shogun''s Ofuda,
    The Reaper, Ancile, Gladiator''s Shield, Riptalon, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.34
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.54
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.96
    Stampede:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - Stampede
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Draconic Scale, Amanita Charm,
    Jotunn''s Revenge, The Crusher, Kinetic Cuirass, Berserker''s Shield, Soul Gem,
    Eye of Providence, Breastplate of Valor, Stone of Binding, Oni Hunter''s Garb,
    Screeching Gargoyle, Spear of the Magus, Void Shield, Avenging Blade, The Cosmic
    Horror, Void Stone, Shield of the Phoenix, Spear of Desolation, Erosion, Spectral
    Armor, Runeforged Hammer, Pharaoh''s Curse, Hydra''s Lament, Yogi''s Necklace,
    Obsidian Shard, Riptalon, Shield Splitter, The Reaper, Silverbranch Bow, Leviathan''s
    Hide, Helm of Radiance, Midgardian Mail, Eye of the Storm, Rod of Asclepius, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.48
    Stampede:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Draconic Scale, Amanita Charm,
    Gluttonous Grimoire, Kinetic Cuirass, Breastplate of Valor, Golden Blade, Eye
    of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher, Jotunn''s Revenge,
    Riptalon, Runeforged Hammer, Lernaean Bow, Hydra''s Lament, Soul Gem, Shogun''s
    Ofuda, Shield of the Phoenix, Tyrfing, Spectral Armor, Silverbranch Bow, Yogi''s
    Necklace, Shield Splitter, Erosion, Eye of the Storm, Bracer of The Abyss, Dominance,
    Death Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Bragi''s Harp, Midgardian Mail, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.33
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.24
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Draconic Scale
  - Stampede
  flex_slots:
  - Draconic Scale
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Draconic Scale, Prophetic Cloak, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass,
    Shield of the Phoenix, Berserker''s Shield, Hydra''s Lament, Soul Gem, Gluttonous
    Grimoire, Eye of Providence, Oni Hunter''s Garb, Hide of the Nemean Lion, The
    Crusher, Chronos'' Pendant, Runeforged Hammer, Screeching Gargoyle, Chandra''s
    Grace, Spear of Desolation, Gladiator''s Shield, Spectral Armor, Erosion, Shield
    Splitter, Yogi''s Necklace, Pharaoh''s Curse, Helm of Radiance, Rod of Asclepius,
    Gem of Focus, Eye of the Storm, Arondight, Death Metal, Leviathan''s Hide, Jade
    Scepter, Midgardian Mail, Spear of the Magus, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.09
      fit: 0.48
    Prophetic Cloak:
      total: 0.53
      efficiency: 0.43
      win: 0.62
      pick: 0.1
      fit: 0.64
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.64
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Draconic Scale
  - The Crusher
  - Stampede
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Draconic Scale, Berserker''s
    Shield, The Crusher, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic
    Cuirass, Breastplate of Valor, Eye of Providence, Runeforged Hammer, Hydra''s
    Lament, Oni Hunter''s Garb, Shield Splitter, Soul Gem, Golden Blade, Lernaean
    Bow, Eye of the Storm, Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral
    Armor, Avenging Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Spear of
    the Magus, Shogun''s Ofuda, Leviathan''s Hide, Dominance, The Cosmic Horror, Helm
    of Radiance, Heartseeker, Rod of Asclepius, Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.38
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Freya's Tears
  - Gluttonous Grimoire
  - Draconic Scale
  - The Crusher
  - Stampede
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Draconic Scale, Gluttonous
    Grimoire, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s
    Shield, Soul Gem, Breastplate of Valor, Eye of Providence, Runeforged Hammer,
    Oni Hunter''s Garb, Hydra''s Lament, Death Metal, Spear of the Magus, Shield Splitter,
    The Cosmic Horror, Helm of Radiance, Shield of the Phoenix, Rod of Asclepius,
    Eye of the Storm, Spectral Armor, Erosion, Spear of Desolation, Jade Scepter,
    Yogi''s Necklace, Pharaoh''s Curse, Avenging Blade, Golden Blade, Obsidian Shard,
    Lernaean Bow, The Reaper, Triton''s Conch, Chronos'' Pendant, Damaru, Leviathan''s
    Hide, Wish-Granting Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.23
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.66
      pick: 0.05
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Stampede:
      total: 0.54
      efficiency: 0.52
      win: 0.71
      pick: 0.06
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Gluttonous Grimoire, Shield of the
    Phoenix, Erosion, Breastplate of Valor, Draconic Scale, Spectral Armor, Shield
    Splitter, Pharaoh''s Curse, Jotunn''s Revenge, Runeforged Hammer, The Crusher,
    Leviathan''s Hide, Soul Gem, Eye of the Storm, Hydra''s Lament, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Yogi''s Necklace, Hide of the Nemean Lion,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Stampede, Ancile, Rod of Asclepius,
    Gladiator''s Shield, Doublet of Binding, Xibalban Effigy, Void Shield, Hussar''s
    Wings, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.17
      fit: 0.37
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.66
      pick: 0.05
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.68
  starter: *id001
---
