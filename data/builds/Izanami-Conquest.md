---
type: smite-build
god: Izanami
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Tyrfing
    pick_rate: 0.6
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.58
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.64
  - name: Odysseus' Bow
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.63
    - name: Dagger of Frenzy
      pick_rate: 0.12
      win_rate: 0.72
  - name: Dominance
    pick_rate: 0.16
    win_rate: 0.68
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.58
    - name: The Executioner
      pick_rate: 0.11
      win_rate: 0.52
  - name: Riptalon
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.53
    - name: Qin's Blade
      pick_rate: 0.11
      win_rate: 0.57
  - name: Qin's Blade
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Riptalon
      pick_rate: 0.1
      win_rate: 0.66
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.57
  - name: Deathbringer
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Qin's Blade
      pick_rate: 0.1
      win_rate: 0.64
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.62
  source_url: https://smitebrain.com/gods/izanami/
  last_verified: '2026-08-01'
  god_win_rate: 0.6
  god_matches_won: 243
  god_matches_played: 405
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Gluttonous Grimoire
  - Riptalon
  - Deathbringer
  flex_slots:
  - Gluttonous Grimoire
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Soul Gem, Death Metal, Lernaean Bow, Damaru, Hydra''s Lament, Genji''s
    Guard, Golden Blade, Runeforged Hammer, Silverbranch Bow, The Reaper, Tekko-Kagi,
    Bragi''s Harp, Spear of the Magus, Breastplate of Valor, Bracer of The Abyss,
    Pharaoh''s Curse, The Cosmic Horror, Demon Blade, Amanita Charm, Spear of Desolation,
    Oni Hunter''s Garb, Nimble Ring, Kinetic Cuirass, Blood-Bound Book, Yogi''s Necklace,
    Bancroft''s Talon, Heartseeker, Avenging Blade, Shogun''s Ofuda, Obsidian Shard,
    Freya''s Tears, Eye of Providence, Chronos'' Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Tyrfing:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.49
    Dominance:
      total: 0.56
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.47
    Deathbringer:
      total: 0.53
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.39
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  - Damaru
  - Deathbringer
  flex_slots:
  - Death Metal
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Death Metal, Soul Gem, Damaru, Lernaean Bow, Genji''s Guard, Hydra''s
    Lament, Golden Blade, Runeforged Hammer, The Reaper, Silverbranch Bow, Breastplate
    of Valor, Spear of the Magus, Tekko-Kagi, Bragi''s Harp, Bracer of The Abyss,
    Pharaoh''s Curse, The Cosmic Horror, Demon Blade, Amanita Charm, Spear of Desolation,
    Oni Hunter''s Garb, Kinetic Cuirass, Blood-Bound Book, Yogi''s Necklace, Bancroft''s
    Talon, Nimble Ring, Heartseeker, Avenging Blade, Freya''s Tears, Obsidian Shard,
    Eye of Providence, Chronos'' Pendant, Musashi''s Dual Swords.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.46
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Dominance:
      total: 0.56
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.36
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.45
    Damaru:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    Deathbringer:
      total: 0.54
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - The Crusher
  - Deathbringer
  flex_slots:
  - Deathbringer
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Riptalon, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, The Crusher,
    Death Metal, Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Spear of the
    Magus, Lernaean Bow, Spear of Desolation, The Cosmic Horror, Damaru, The Reaper,
    Breastplate of Valor, Runeforged Hammer, Silverbranch Bow, Bracer of The Abyss,
    Bragi''s Harp, Golden Blade, Obsidian Shard, Tekko-Kagi, Chronos'' Pendant, Blood-Bound
    Book, Bancroft''s Talon, Amanita Charm, Rod of Asclepius, Pharaoh''s Curse, Oni
    Hunter''s Garb, Heartseeker, Kinetic Cuirass, Nimble Ring, Yogi''s Necklace, Helm
    of Radiance, Freya''s Tears, The World Stone, Doom Orb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.4
    Dominance:
      total: 0.55
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.3
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.43
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Deathbringer:
      total: 0.52
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Tyrfing
  - Dominance
  - Riptalon
  - Deathbringer
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Amanita Charm, Soul Gem, Berserker''s Shield, Gluttonous Grimoire,
    Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Genji''s Guard, The
    Reaper, The Crusher, Jotunn''s Revenge, Eye of Providence, Blood-Bound Book, Bancroft''s
    Talon, Oni Hunter''s Garb, Chandra''s Grace, Runeforged Hammer, Pharaoh''s Curse,
    Death Metal, Golden Blade, Hydra''s Lament, Breastplate of Valor, Lernaean Bow,
    Damaru, Yogi''s Necklace, Freya''s Tears, Lifebinder, Phoenix Feather, Shogun''s
    Ofuda, Shifter''s Shield, Spectral Armor, Shield Splitter, Eye of the Storm, Erosion,
    Umbral Link, Spear of the Magus, Avenging Blade, Bloodforge, Silverbranch Bow.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Tyrfing:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.36
    Dominance:
      total: 0.54
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.26
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.62
    Deathbringer:
      total: 0.51
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.26
    Amanita Charm:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - The Crusher
  - Deathbringer
  flex_slots:
  - Jotunn's Revenge
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Riptalon, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Soul
    Gem, Berserker''s Shield, Silverbranch Bow, The Reaper, Spear of the Magus, Death
    Metal, Avenging Blade, Genji''s Guard, Lernaean Bow, Hydra''s Lament, Tekko-Kagi,
    The Cosmic Horror, Damaru, Spear of Desolation, Screeching Gargoyle, Runeforged
    Hammer, Golden Blade, Heartseeker, Obsidian Shard, Breastplate of Valor, Bracer
    of The Abyss, Bragi''s Harp, Amanita Charm, Pharaoh''s Curse, Stone of Binding,
    Titan''s Bane, Oni Hunter''s Garb, Kinetic Cuirass, Pendulum Blade, Yogi''s Necklace,
    Void Shield, Toxic Blade, The World Stone, Doom Orb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Tyrfing:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.42
    Dominance:
      total: 0.55
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.32
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Deathbringer:
      total: 0.52
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Dagger of Frenzy
  - Dominance
  - Gluttonous Grimoire
  - Riptalon
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Gluttonous Grimoire
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Golden Blade, Soul Gem, Silverbranch Bow, Lernaean Bow, Death Metal,
    Genji''s Guard, Hydra''s Lament, Damaru, Runeforged Hammer, Breastplate of Valor,
    Bracer of The Abyss, Spear of the Magus, Pharaoh''s Curse, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Amanita Charm, The Cosmic Horror, Oni Hunter''s Garb, Kinetic
    Cuirass, Yogi''s Necklace, Toxic Blade, Blood-Bound Book, Spear of Desolation,
    Nimble Ring, Bancroft''s Talon, Demon Blade, Shogun''s Ofuda, Eye of Providence,
    Freya''s Tears, Avenging Blade, Rod of Asclepius, Chronos'' Pendant.'
  slot_scores:
    Tyrfing:
      total: 0.56
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.59
    Dagger of Frenzy:
      total: 0.52
      efficiency: 0.4
      win: 0.72
      pick: 0.12
      fit: 0.37
    Dominance:
      total: 0.55
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Riptalon:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.14
      fit: 0.57
    Deathbringer:
      total: 0.52
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Riptalon, Soul Gem, Jotunn''s Revenge,
    Genji''s Guard, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The
    Crusher, Breastplate of Valor, Death Metal, Spear of Desolation, Chronos'' Pendant,
    Lernaean Bow, Damaru, Freya''s Tears, Shield of the Phoenix, Spear of the Magus,
    Runeforged Hammer, Bracer of The Abyss, Golden Blade, The Cosmic Horror, Silverbranch
    Bow, Gem of Focus, Arondight, Amanita Charm, Bragi''s Harp, Screeching Gargoyle,
    Pharaoh''s Curse, Chandra''s Grace, Blood-Bound Book, The Reaper, Oni Hunter''s
    Garb, Kinetic Cuirass, Bancroft''s Talon, Yogi''s Necklace, Pendulum Blade, Rod
    of Asclepius, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Tyrfing:
      total: 0.53
      efficiency: 0.49
      win: 0.6
      pick: 0.6
      fit: 0.37
    Dominance:
      total: 0.54
      efficiency: 0.54
      win: 0.68
      pick: 0.16
      fit: 0.27
    Deathbringer:
      total: 0.51
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.27
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Berserker''s Shield, Soul Gem, Death Metal, Lernaean Bow, Damaru, Riptalon, Hydra''s
    Lament, Genji''s Guard, Golden Blade, Runeforged Hammer, Silverbranch Bow, The
    Reaper, Tekko-Kagi, Bragi''s Harp, Spear of the Magus, Breastplate of Valor, Bracer
    of The Abyss, Pharaoh''s Curse, The Cosmic Horror, Demon Blade, Amanita Charm,
    Spear of Desolation, Oni Hunter''s Garb, Nimble Ring, Kinetic Cuirass, Blood-Bound
    Book, Yogi''s Necklace, Bancroft''s Talon, Heartseeker, Avenging Blade, Shogun''s
    Ofuda, Obsidian Shard, Freya''s Tears, Eye of Providence, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Deathbringer
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Berserker''s Shield, Soul Gem, Death Metal, Lernaean Bow, Damaru,
    Riptalon, Hydra''s Lament, Genji''s Guard, Golden Blade, Runeforged Hammer, Silverbranch
    Bow, The Reaper, Tekko-Kagi, Bragi''s Harp, Spear of the Magus, Breastplate of
    Valor, Bracer of The Abyss, Pharaoh''s Curse, The Cosmic Horror, Demon Blade,
    Amanita Charm, Spear of Desolation, Oni Hunter''s Garb, Nimble Ring, Kinetic Cuirass,
    Blood-Bound Book, Yogi''s Necklace, Bancroft''s Talon, Heartseeker, Avenging Blade,
    Shogun''s Ofuda, Obsidian Shard, Freya''s Tears, Eye of Providence, Chronos''
    Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Deathbringer:
      total: 0.53
      efficiency: 0.37
      win: 0.75
      pick: 0.12
      fit: 0.39
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.48
  swaps:
  - added: Deathbringer
    removed: Death Metal
    reason: community 75% win over 49 matches (vs 60% on this god), taking the model's
      weakest slot from Death Metal
  starter: *id001
---
